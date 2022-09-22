FROM ghcr.io/observatorycontrolsystem/observation-portal:4.4.4

WORKDIR /overrides

COPY ./ ./

ENV DJANGO_SETTINGS_MODULE=settings
