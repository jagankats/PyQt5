import pyowm


class OpenWeatherMap:
    def __init__(self):
        # free OWM Current Weather API KEY & Authentication
        weather_key = '6d9133401bea7fe7de583a4c82051ade'
        weather_owm = pyowm.OWM(weather_key)
        weather_mgr = weather_owm.weather_manager()

        # Search for current weather in London (Great Britain) and get details
        location = weather_mgr.weather_at_place('Ludhiana,IN')
        self.weather_report = location.weather

        # attach degree celsius symbol to all temperature related variables
        self.degree_celsius = str(u"\N{DEGREE SIGN}") + 'C'

        # free OWM Agro API KEY & Authentication
        agro_key = '6806e5beb9f9bb31ff3b69cd6feffe26'
        agro_owm = pyowm.OWM(agro_key)
        agro_mgr = agro_owm.agro_manager()

        # free OWM Agro API Polygon id & Authentication
        pol_id = '612ca3cba81b762fa367ee2a'
        field_polygon = agro_mgr.get_polygon(pol_id)
        self.soil = agro_mgr.soil_data(field_polygon)


    def weather_condition(self):
        # to get reference time of connection
        ref_time = str(self.weather_report.reference_time(timeformat='date').strftime('%d-%b-%Y %H:%M:%S'))
        # print(ref_time)

        # get the status of weather condition
        status = str(self.weather_report.detailed_status)
        # print(status)

        # get the speed of wind in km/hour
        wind_speed = str(self.weather_report.wind()['speed'])+' km/h'
        # print(wind_speed)

        # for humidity percentage
        humidity = str(self.weather_report.humidity)+' %'
        # print(humidity)

        current_temp = str(self.weather_report.temperature('celsius')['temp'])+self.degree_celsius
        max_temp = str(self.weather_report.temperature('celsius')['temp_max'])+self.degree_celsius
        min_temp = str(self.weather_report.temperature('celsius')['temp_min'])+self.degree_celsius
        feels_like_temp = str(self.weather_report.temperature('celsius')['feels_like'])+self.degree_celsius
        # print(current_temp, max_temp, min_temp, feels_like_temp)

        # to get the percentage of clouds in weather
        clouds = str(self.weather_report.clouds) + ' %'
        # print(clouds)

        return ref_time, status, wind_speed, humidity, current_temp, max_temp, \
               min_temp, feels_like_temp, clouds

    def soil_report(self):
        # to get temperature of the soil surface
        surface_temp = str(self.soil.surface_temp(unit='celsius'))+self.degree_celsius
        # print(surface_temp)

        # to get the temperature of soil at 10cm of depth
        temp_at_10cm = str(self.soil.ten_cm_temp(unit='celsius'))+self.degree_celsius
        # print(temp_at_10cm)

        # to get moisture content in soil
        soil_moisture = str(self.soil.moisture*100) + ' %'
        # print(soil_moisture)

        return surface_temp, temp_at_10cm, soil_moisture

