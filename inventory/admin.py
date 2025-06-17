from django.contrib import admin
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from .models import InventoryManagement
from import_export.widgets import DateWidget, BooleanWidget

class InventoryManagementResource(resources.ModelResource):
    vehicle_no = fields.Field(attribute='vehicle_no', column_name='Vehicle No')
    chassis_no = fields.Field(attribute='chassis_no', column_name='Chassis No')
    model = fields.Field(attribute='model', column_name='Model')
    oem = fields.Field(attribute='oem', column_name='OEM')
    onboarding_date = fields.Field(attribute='onboarding_date', column_name='Onboarding Date')
    registration_date = fields.Field(attribute='registration_date', column_name='Registration Date')
    vehicle_type_id = fields.Field(attribute='vehicle_type_id', column_name='Vehicle Type ID')
    city = fields.Field(attribute='city', column_name='City')
    ownership = fields.Field(attribute='ownership', column_name='Ownership')
    provider = fields.Field(attribute='provider', column_name='Provider')
    load_capacity = fields.Field(attribute='load_capacity', column_name='Load Capacity')
    battery_no = fields.Field(attribute='battery_no', column_name='Battery No')
    charger_no = fields.Field(attribute='charger_no', column_name='Charger No')
    stepney = fields.Field(attribute='stepney', column_name='Stepney')
    toolkits = fields.Field(attribute='toolkits', column_name='Toolkits')
    iot_provider = fields.Field(attribute='iot_provider', column_name='IOT Provider')
    iot_no = fields.Field(attribute='iot_no', column_name='IOT No')
    rc_copy = fields.Field(attribute='rc_copy', column_name='RC Copy')
    rc_upload = fields.Field(attribute='rc_upload', column_name='RC Upload')
    insurance_copy = fields.Field(attribute='insurance_copy', column_name='Insurance Copy')
    insurance_due = fields.Field(attribute='insurance_due', column_name='Insurance Due')
    lease_per_month = fields.Field(attribute='lease_per_month', column_name='Lease ?/month')
    number_plate_photo = fields.Field(attribute='number_plate_photo', column_name='Number Plate Photo')
    branding_photo_1 = fields.Field(attribute='branding_photo_1', column_name='Branding Photo 1')
    branding_photo_2 = fields.Field(attribute='branding_photo_2', column_name='Branding Photo 2')
    branding_photo_3 = fields.Field(attribute='branding_photo_3', column_name='Branding Photo 3')
    branding_photo_4 = fields.Field(attribute='branding_photo_4', column_name='Branding Photo 4')
    reason = fields.Field(attribute='reason', column_name='Reason')
    state = fields.Field(attribute='state', column_name='State')
    parking_type = fields.Field(attribute='parking_type', column_name='Parking Type')
    hub_address = fields.Field(attribute='hub_address', column_name='Hub Address')
    parking_location = fields.Field(attribute='parking_location', column_name='Parking Location')
    returning_date = fields.Field(attribute='returning_date', column_name='Returning Date')
    returning_reason = fields.Field(attribute='returning_reason', column_name='Returning Reason')
    replacement_vehicle = fields.Field(attribute='replacement_vehicle', column_name='Replacement Vehicle')
    rto_compliance = fields.Field(attribute='rto_compliance', column_name='RTO Compliance')
    allowed_kms = fields.Field(attribute='allowed_kms', column_name='Allowed KMs')

    onboarding_date = fields.Field(
        attribute='onboarding_date',
        column_name='Onboarding Date',
        widget=DateWidget(format='%Y-%m-%d')
    )
    registration_date = fields.Field(
        attribute='registration_date',
        column_name='Registration Date',
        widget=DateWidget(format='%Y-%m-%d')
    )
    returning_date = fields.Field(
        attribute='returning_date',
        column_name='Returning Date',
        widget=DateWidget(format='%Y-%m-%d')
    )
    stepney = fields.Field(
        attribute='stepney',
        column_name='Stepney',
        widget=BooleanWidget()
    )
    toolkits = fields.Field(
        attribute='toolkits',
        column_name='Toolkits',
        widget=BooleanWidget()
    )
    rc_copy = fields.Field(
        attribute='rc_copy',
        column_name='RC Copy',
        widget=BooleanWidget()
    )
    rto_compliance = fields.Field(
        attribute='rto_compliance',
        column_name='RTO Compliance',
        widget=BooleanWidget()
    )
    
    class Meta:
        model = InventoryManagement
        import_id_fields = ('vehicle_no',)  # ya koi unique field
        skip_unchanged = True
        report_skipped = True

class InventoryManagementAdmin(ImportExportModelAdmin):
    resource_class = InventoryManagementResource
    list_display = (
        'vehicle_no', 'chassis_no', 'model', 'oem_id', 'onboarding_date', 'registration_date',
        'vehicle_type_id', 'city_id', 'ownership_id', 'provider_id', 'load_capacity', 'battery_no',
        'charger_no', 'stepney', 'toolkits', 'iot_provider', 'iot_no', 'rc_copy', 'rc_upload',
        'insurance_copy', 'insurance_renewal_due', 'lease_per_month', 'number_plate_photo',
        'branding_photo_1', 'branding_photo_2', 'branding_photo_3', 'branding_photo_4',
        'reason', 'state', 'parking_type', 'hub_address', 'parking_location', 'returning_date',
        'returning_reason', 'replacement_vehicle', 'rto_compliance', 'allowed_kms'
    )

admin.site.register(InventoryManagement, InventoryManagementAdmin)