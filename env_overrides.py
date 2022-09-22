import os

# Set environment variables you want below here for development, or within the docker deployment:
# -----------------------------------------------------------------------------------------------

# Serializer class overrides. Uncomment and edit the location to point to your class override
# os.environ['OBSERVATIONS_SUMMARY_SERIALIZER'] = 'observation_portal.observations.serializers.SummarySerializer'
# os.environ['OBSERVATIONS_CONFIGURATIONSTATUS_SERIALIZER'] = 'observation_portal.observations.serializers.ConfigurationStatusSerializer'
# os.environ['OBSERVATIONS_TARGET_SERIALIZER'] = 'observation_portal.observations.serializers.ObservationTargetSerializer'
# os.environ['OBSERVATIONS_CONFIGURATION_SERIALIZER'] = 'observation_portal.observations.serializers.ObservationConfigurationSerializer'
# os.environ['OBSERVATIONS_REQUEST_SERIALIZER'] = 'observation_portal.observations.serializers.ObserveRequestSerializer'
# os.environ['OBSERVATIONS_REQUESTGROUP_SERIALIZER'] = 'observation_portal.observations.serializers.ObserveRequestGroupSerializer'
# os.environ['OBSERVATIONS_SCHEDULE_SERIALIZER'] = 'observation_portal.observations.serializers.ScheduleSerializer'
# os.environ['OBSERVATIONS_OBSERVATION_SERIALIZER'] = 'observation_portal.observations.serializers.ObservationSerializer'
# os.environ['OBSERVATIONS_CANCEL_SERIALIZER'] = 'observation_portal.observations.serializers.CancelObservationsSerializer'
# os.environ['OBSERVATIONS_CANCEL_RESPONSE_SERIALIZER'] = 'observation_portal.observations.serializers.CancelObservationsResponseSerializer'
# os.environ['OBSERVATIONS_LAST_SCHEDULED_SERIALIZER'] = 'observation_portal.observations.serializers.LastScheduledSerializer'
# os.environ['OBSERVATIONS_OBSERVATIONFILTERS_SERIALIZER'] = 'observation_portal.observations.serializers.ObservationFiltersSerializer'

# os.environ['REQUESTGROUPS_CADENCE_SERIALIZER'] = 'observation_portal.requestgroups.serializers.CadenceSerializer'
# os.environ['REQUESTGROUPS_CADENCEREQUEST_SERIALIZER'] = 'observation_portal.requestgroups.serializers.CadenceRequestSerializer'
# os.environ['REQUESTGROUPS_CONSTRAINTS_SERIALIZER'] = 'observation_portal.requestgroups.serializers.ConstraintsSerializer'
# os.environ['REQUESTGROUPS_REGIONOFINTEREST_SERIALIZER'] = 'observation_portal.requestgroups.serializers.RegionOfInterestSerializer'
# os.environ['REQUESTGROUPS_INSTRUMENTCONFIG_SERIALIZER'] = 'observation_portal.requestgroups.serializers.InstrumentConfigSerializer'
# os.environ['REQUESTGROUPS_ACQUISITIONCONFIG_SERIALIZER'] = 'observation_portal.requestgroups.serializers.AcquisitionConfigSerializer'
# os.environ['REQUESTGROUPS_GUIDINGCONFIG_SERIALIZER'] = 'observation_portal.requestgroups.serializers.GuidingConfigSerializer'
# os.environ['REQUESTGROUPS_TARGET_SERIALIZER'] = 'observation_portal.requestgroups.serializers.TargetSerializer'
# os.environ['REQUESTGROUPS_CONFIGURATION_SERIALIZER'] = 'observation_portal.requestgroups.serializers.ConfigurationSerializer'
# os.environ['REQUESTGROUPS_LOCATION_SERIALIZER'] = 'observation_portal.requestgroups.serializers.LocationSerializer'
# os.environ['REQUESTGROUPS_WINDOW_SERIALIZER'] = 'observation_portal.requestgroups.serializers.WindowSerializer'
# os.environ['REQUESTGROUPS_REQUEST_SERIALIZER'] = 'observation_portal.requestgroups.serializers.RequestSerializer'
# os.environ['REQUESTGROUPS_REQUESTGROUP_SERIALIZER'] = 'observation_portal.requestgroups.serializers.RequestGroupSerializer'
# os.environ['REQUESTGROUPS_DRAFTREQUESTGROUP_SERIALIZER'] = 'observation_portal.requestgroups.serializers.DraftRequestGroupSerializer'
# os.environ['REQUESTGROUPS_DITHER_SERIALIZER'] = 'observation_portal.requestgroups.serializers.DitherSerializer'
# os.environ['REQUESTGROUPS_MOSAIC_SERIALIZER'] = 'observation_portal.requestgroups.serializers.MosaicSerializer'
# os.environ['REQUESTGROUPS_LAST_CHANGED_SERIALIZER'] = 'observation_portal.requestgroups.serializers.LastChangedSerializer'

# os.environ['PROPOSALS_PROPOSAL_SERIALIZER'] = 'observation_portal.proposals.serializers.ProposalSerializer'
# os.environ['PROPOSALS_PROPOSALINVITE_SERIALIZER'] = 'observation_portal.proposals.serializers.ProposalInviteSerializer'
# os.environ['PROPOSALS_SEMESTER_SERIALIZER'] = 'observation_portal.proposals.serializers.SemesterSerialzer'
# os.environ['PROPOSALS_MEMBERSHIP_SERIALIZER'] = 'observation_portal.proposals.serializers.MembershipSerializer'
# os.environ['PROPOSALS_PROPOSALNOTIFICATION_SERIALIZER'] = 'observation_portal.proposals.serializers.ProposalNotificationSerializer'
# os.environ['PROPOSALS_PROPOSALNOTIFICATION_RESPONSE_SERIALIZER'] = 'observation_portal.proposals.serializers.ProposalNotificationResponseSerializer'
# os.environ['PROPOSALS_TIMELIMIT_SERIALIZER'] = 'observation_portal.proposals.serializers.TimeLimitSerializer'
# os.environ['PROPOSALS_TIMELIMIT_RESPONSE_SERIALIZER'] = 'observation_portal.proposals.serializers.TimeLimitResponseSerializer'
# os.environ['PROPOSALS_TIMEALLOCATION_SERIALIZER'] = 'observation_portal.proposals.serializers.TimeAllocationSerializer'

# os.environ['ACCOUNTS_PROFILE_SERIALIZER'] = 'observation_portal.accounts.serializers.ProfileSerializer'
# os.environ['ACCOUNTS_USER_SERIALIZER'] = 'observation_portal.accounts.serializers.UserSerializer'
# os.environ['ACCOUNTS_ACCOUNTREMOVAL_SERIALIZER'] = 'observation_portal.accounts.serializers.AccountRemovalSerializer'
# os.environ['ACCOUNTS_ACCEPTTERMS_SERIALIZER'] = 'observation_portal.accounts.serializers.AcceptTermsResponseSerializer'
# os.environ['ACCOUNTS_REVOKETOKEN_SERIALIZER'] = 'observation_portal.accounts.serializers.RevokeTokenResponseSerializer'
# os.environ['ACCOUNTS_ACCOUNTREMOVAL_RESPONSE_SERIALIZER'] = 'observation_portal.accounts.serializers.AccountRemovalResponseSerializer'
# os.environ['ACCOUNTS_CREATEUSER_SERIALIZER'] = 'observation_portal.accounts.serializers.CreateUserSerializer'
# os.environ['ACCOUNTS_BULKCREATEUSERS_SERIALIZER'] = 'observation_portal.accounts.serializers.BulkCreateUsersSerializer'

# os.environ['SCIAPPLICATIONS_CALL_SERIALIZER'] = 'observation_portal.sciapplications.serializers.CallSerializer'
# os.environ['SCIAPPLICATIONS_SCIENCEAPPLICATION_SERIALIZER'] = 'observation_portal.sciapplications.serializers.ScienceApplicationSerializer'

# as_dict method overrides. Uncomment and edit the location to point to your method override. This is for modifying list/detail view output.
# os.environ['OBSERVATIONS_SUMMARY_AS_DICT'] = 'observation_portal.observations.models.summary_as_dict'
# os.environ['OBSERVATIONS_CONFIGURATIONSTATUS_AS_DICT'] = 'observation_portal.observations.models.configurationstatus_as_dict'
# os.environ['OBSERVATIONS_OBSERVATION_AS_DICT'] = 'observation_portal.observations.models.observation_as_dict'

# os.environ['REQUESTGROUPS_CONSTRAINTS_AS_DICT'] = 'observation_portal.requestgroups.models.constraints_as_dict'
# os.environ['REQUESTGROUPS_REGIONOFINTEREST_AS_DICT'] = 'observation_portal.requestgroups.models.regionofinterest_as_dict'
# os.environ['REQUESTGROUPS_INSTRUMENTCONFIG_AS_DICT'] = 'observation_portal.requestgroups.models.instrumentconfig_as_dict'
# os.environ['REQUESTGROUPS_ACQUISITIONCONFIG_AS_DICT'] = 'observation_portal.requestgroups.models.acquisitionconfig_as_dict'
# os.environ['REQUESTGROUPS_GUIDINGCONFIG_AS_DICT'] = 'observation_portal.requestgroups.models.guidingconfig_as_dict'
# os.environ['REQUESTGROUPS_TARGET_AS_DICT'] = 'observation_portal.requestgroups.models.target_as_dict'
# os.environ['REQUESTGROUPS_CONFIGURATION_AS_DICT'] = 'observation_portal.requestgroups.models.configuration_as_dict'
# os.environ['REQUESTGROUPS_LOCATION_AS_DICT'] = 'observation_portal.requestgroups.models.location_as_dict'
# os.environ['REQUESTGROUPS_WINDOW_AS_DICT'] = 'observation_portal.requestgroups.models.window_as_dict'
# os.environ['REQUESTGROUPS_REQUEST_AS_DICT'] = 'observation_portal.requestgroups.models.request_as_dict'
# os.environ['REQUESTGROUPS_REQUESTGROUP_AS_DICT'] = 'observation_portal.requestgroups.models.requestgroup_as_dict'

# os.environ['PROPOSALS_PROPOSAL_AS_DICT'] = 'observation_portal.proposals.models.proposal_as_dict'
# os.environ['PROPOSALS_MEMBERSHIP_AS_DICT'] = 'observation_portal.proposals.models.membership_as_dict'
# os.environ['PROPOSALS_TIMEALLOCATION_AS_DICT'] = 'observation_portal.proposals.models.timeallocation_as_dict'

# duration method overrides
# os.environ['INSTRUMENT_CONFIGURATION_PER_EXPOSURE_DURATION'] = 'observation_portal.requestgroups.duration_utils.get_instrument_configuration_duration_per_exposure'
