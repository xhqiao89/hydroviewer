from tethys_sdk.base import TethysAppBase, url_map_maker
from tethys_sdk.app_settings import CustomSetting

base_name = __package__.split('.')[-1]
base_url = base_name.replace('_', '-')

class Hydroviewer(TethysAppBase):
    """
    Tethys app class for HydroViewer.
    """

    name = 'HydroViewer {0}'.format(base_name.split('_')[-1].title())
    index = '{0}:home'.format(base_name)
    icon = '{0}/images/logo.png'.format(base_name)
    package = '{0}'.format(base_name)
    root_url = base_url
    color = '#425e17'
    description = 'Place a brief description of your app here.'
    tags = 'Hydrology'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url=base_url,
                controller='{0}.controllers.home'.format(base_name)),
            UrlMap(
                name='ecmwf',
                url='ecmwf-rapid',
                controller='{0}.controllers.ecmwf'.format(base_name)),
            UrlMap(
                name='lis',
                url='lis-rapid',
                controller='{0}.controllers.lis'.format(base_name)),
            UrlMap(
                name='get-available-dates',
                url='ecmwf-rapid/get-available-dates',
                controller='{0}.controllers.get_available_dates'.format(base_name)),
            UrlMap(
                name='get-time-series',
                url='ecmwf-rapid/get-time-series',
                controller='{0}.controllers.ecmwf_get_time_series'.format(base_name)),
            UrlMap(
                name='get-time-series',
                url='lis-rapid/get-time-series',
                controller='{0}.controllers.lis_get_time_series'.format(base_name)),
            UrlMap(
                name='get-return-periods',
                url='ecmwf-rapid/get-return-periods',
                controller='{0}.controllers.get_return_periods'.format(base_name)),
            UrlMap(
                name='get-warning-points',
                url='ecmwf-rapid/get-warning-points',
                controller='{0}.controllers.get_warning_points'.format(base_name)),
            UrlMap(
                name='get-historic-data',
                url='ecmwf-rapid/get-historic-data',
                controller='{0}.controllers.get_historic_data'.format(base_name)),
            UrlMap(
                name='get-flow-duration-curve',
                url='ecmwf-rapid/get-flow-duration-curve',
                controller='{0}.controllers.get_flow_duration_curve'.format(base_name)),
            UrlMap(
                name='get_historic_data_csv',
                url='ecmwf-rapid/get-historic-data-csv',
                controller='{0}.controllers.get_historic_data_csv'.format(base_name)),
            UrlMap(
                name='get_forecast_data_csv',
                url='ecmwf-rapid/get-forecast-data-csv',
                controller='{0}.controllers.get_forecast_data_csv'.format(base_name)),
            UrlMap(
                name='get_forecast_data_csv',
                url='lis-rapid/get-forecast-data-csv',
                controller='{0}.controllers.get_lis_data_csv'.format(base_name)),
            UrlMap(
                name='get_lis_shp',
                url='lis-rapid/get-lis-shp',
                controller='{0}.controllers.shp_to_geojson'.format(base_name)),
        )

        return url_maps


    def custom_settings(self):
        """
        Custom app settings.
        """
        return (
            CustomSetting(
                name='api_source',
                type=CustomSetting.TYPE_STRING,
                description='Tethys portal where Streamflow Prediction Tool is installed',
                required=True
            ),
            CustomSetting(
                name='spt_token',
                type=CustomSetting.TYPE_STRING,
                description='Unique token to access data from the Streamflow Prediction Tool',
                required=True
            ),
            CustomSetting(
                name='geoserver',
                type=CustomSetting.TYPE_STRING,
                description='Spatial dataset service for app to use',
                required=True
            ),
            CustomSetting(
                name='workspace',
                type=CustomSetting.TYPE_STRING,
                description='Workspace within Geoserver where web service is',
                required=True
            ),
            CustomSetting(
                name='region',
                type=CustomSetting.TYPE_STRING,
                description='Streamflow Prediction Tool Region',
                required=True
            ),
            CustomSetting(
                name='keywords',
                type=CustomSetting.TYPE_STRING,
                description='Keyword(s) for visualizing watersheds in HydroViewer',
                required=True
            ),
            CustomSetting(
                name='zoom_info',
                type=CustomSetting.TYPE_STRING,
                description='lon,lat,zoom_level',
                required=True
            ),
            CustomSetting(
                name='default_model_type',
                type=CustomSetting.TYPE_STRING,
                description='Default Model Type : (Options : ECMWF-RAPID, LIS-RAPID)',
                required=False
            ),
            CustomSetting(
                name='default_watershed_name',
                type=CustomSetting.TYPE_STRING,
                description='Default Watershed Name: (For ex: "South America (Brazil)") ',
                required=False
            ),
            CustomSetting(
                name='lis_path',
                type=CustomSetting.TYPE_STRING,
                description='Path to local LIS-RAPID directory',
                required=False
            ),
        )