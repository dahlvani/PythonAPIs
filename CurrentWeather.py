import re, urllib, json

def get_ip():
    url = "http://checkip.dyndns.org"
    data = urllib.urlopen(url).read()
    ip_address = data[-30:-16]
    return ip_address


def get_weather(ip_address):
    end_point = "http://api.worldweatheronline.com/free/v1/weather.ashx?"
    query = "key=d39cce2fdf5f442d9c3174433191101=" + str(ip_address) + "&num_of_days=0&format=json"
    url = end_point +  query
    json_data = urllib.urlopen(url).read()
    data = json.loads(json_data)
    current_weather = data['data']['current_condition'][0]
    return current_weather


def print_weather(data):
    print """
    Weather : %s
    Temperatue : %s Fahrenheit
    Wind : %s Miles
    Precipitation : %s Inches
    """ % (data['weatherDesc'][0]['value'], data['temp_F'], data['windspeedMiles'], data['precipInches'])


def main():
    print "\nGetting your location's weather information :)"
    ip_address = get_ip()
    data = get_weather(ip_address)
    print_weather(data)


if __name__ == "__main__":
    main()
