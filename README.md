# Observation Portal Project

Library: ![Build](https://github.com/observatorycontrolsystem/observation-portal/workflows/Build/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/observatorycontrolsystem/observation-portal/badge.svg?branch=master)](https://coveralls.io/github/observatorycontrolsystem/observation-portal?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/9846cee7c4904cae8864525101030169)](https://www.codacy.com/gh/observatorycontrolsystem/observation-portal?utm_source=github.com&utm_medium=referral&utm_content=observatorycontrolsystem/observation-portal&utm_campaign=Badge_Grade)

This project provides a forkable base that can be used to customize an Observation Portal instance. The settings.py just imports the base libraries settings, but additional settings can be added to override where appropriate. Currently, customization can be done in several ways:

1. Specifying your own Serializers for each model, allowing for observatory specific validation rules to be added.
2. Defining generic modes, optical elements, and adding instrument and mode specific cerberus validation schemas to Configdb.
3. Overriding settings directly in settings.py or using environment variables to override settings.
4. If all else fails, the base Observation Portal library can be forked and modified, and you can submit a pull request the features are generally useful.

For more information on this project, please see the [base Observation Portal library here](https://github.com/observatorycontrolsystem/observation-portal)


## Prerequisites

Optional prerequisites can be skipped for reduced functionality.

-   Python >= 3.6
-   PostgreSQL >= 9.6
-   A running [Configuration Database](https://github.com/observatorycontrolsystem/configdb) 
-   (Optional) A running [Downtime Database](https://github.com/observatorycontrolsystem/downtime)
-   (Optional) A running Elasticsearch


## Local Development

### **Set up external services**

Please refer to the [Configuration Database](https://github.com/observatorycontrolsystem/configdb) and [Downtime Database](https://github.com/LCOGT/downtime) projects for instructions on how to get those running, as well as the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/5.6/install-elasticsearch.html) for options on how to run Elasticsearch.

### **Set up a [virtual environment](https://docs.python.org/3/tutorial/venv.html)**

Using a virtual environment is highly recommended. Run the following commands from the base of this project. `(env)`
is used to denote commands that should be run using your virtual environment.

    python3 -m venv env
    source env/bin/activate
    (env) pip install numpy && pip install -r requirements.txt

### **Set up the database**

This example uses the [PostgreSQL Docker image](https://hub.docker.com/_/postgres) to create a database. Make sure that the options that you use to set up your database correspond with your configured database settings.

    docker run --name observation-portal-postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=observation_portal -v/var/lib/postgresql/data -p5432:5432 -d postgres:11.1

After creating the database, migrations must be applied to set up the tables in the database.

    (env) python manage.py migrate

### **Run the portal**

    (env) python manage.py runserver

The observation portal should now be accessible from <http://127.0.0.1:8000>!

### **Run local unit tests**

If you override serializers with your own behaviour, you should write some unit tests to ensure they are working properly. Take a look at the base libraries unit test files for helper functions you can import to make writing unit tests easier. You can run local unit tests in a test* file or package with:

    (env) python manage.py test --settings=test_settings


## Overriding Serializers
Overriding the default Serializers allows customizable validation for the different models.

### Example: Target finder chart
If your Observatory requires request submissions to contain a link to a finder chart with each Target, you could override the Target serializer to enforce that the Target's `extra_params` json field contains a `finder_chart_url` that is a url. To accomplish this, you would create a file in the `serializers` package of this project that looks something like this:


```python
from rest_framework import serializers
from django.utils.translation import ugettext as _
from django.core.validators import URLValidator

from observation_portal.requestgroups.serializers import TargetSerializer


class MyTargetSerializer(TargetSerializer):
    def validate(self, data):
        data = super().validate(data)
        if 'finder_chart_url' not in data.get('extra_params', {}):
            raise serializers.ValidationError(_("Must supply a `finder_chart_url` within Target's extra_params."))
        try:
            URLValidator()(data['extra_params']['finder_chart_url'])
        except ValidationError:
             raise serializers.ValidationError(_("Invalid url for `finder_chart_url` within Target's extra_params."))
        return data
```

Then in env_overrides.py, which are imported into the local settings.py prior to importing the library's settings, set the environment variable to point to your serializer dotpath:

```os.environ['REQUESTGROUPS_TARGET_SERIALIZER'] = 'observation_portal.serializers.my_serializer_file.MyTargetSerializer'```

Make sure your custom serializer extends the base serializer and runs it's validate method when overriding if you want the built in validation for that model to continue. A full list of the environment variables for overriding serializers can be found in the [library's settings.py](https://github.com/observatorycontrolsystem/observation-portal/blob/master/observation_portal/settings.py#L287)
