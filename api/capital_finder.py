from ast import parse
from http.server import BaseHTTPRequestHandler
from datetime import datetime
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

    if "country" in query_dict:
      url = "https://restcountries.com/v3.1/name/"
      response = requests.get(url + query_dict["country"])
      data = response.json()
      cap_cities = []

      for country_data in data:
        cap_name = country_data["capital"][0]

        cap_cities.append(cap_name)

      string_cap = str(cap_cities)
      country = query_dict["country"]
      message = f"The capital of {country} is {cap_cities[0]}"
    else:
      message = "name a country"

    self.wfile.write(message.encode())
    return
