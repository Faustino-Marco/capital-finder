from ast import parse
from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()

    url_components = parse.urlsplit(self.path)

    query_string_list = parse.parse_qsl(url_components.query)

    query_dict = dict(query_string_list)
    print("query_dict: ", query_dict)

    if "country" in query_dict:
      url = "https://restcountries.com/v3.1/name/"
      response = requests.get(url + query_dict["country"])
      data = response.json()
      cap_cities = [] 

      for country_data in data:
        cap_name = country_data["capital"]
        print(cap_name)

        cap_cities.append(cap_name)

     
      country = query_dict["country"]
      message = f"The capital of {country} is {cap_cities[0][0]}."

    if "capital" in query_dict:
      url = "https://restcountries.com/v3.1/capital/"
      response = requests.get(url + query_dict["capital"])
      data = response.json()
      home_country = []

      for city_data in data:
        country_name = city_data["name"]["official"]

        home_country.append(country_name)

      
      city = query_dict["capital"]
      message = f"{city} is the capital of {country_name}."
    

    self.wfile.write(message.encode())
    return
