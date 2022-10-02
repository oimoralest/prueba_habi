import subprocess
import unittest
from time import sleep

import requests

from enums import HOST, PORT


class CasasEndpointTestCase(unittest.TestCase):
    """All tests related to /casas/*"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.server = subprocess.Popen(["python3", "main.py"])

        # Needed so server can open the port for requests
        sleep(5)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.server.kill()

    def test_casas_preventa_status_code_200(self):
        """
        Test:
            * /casas/preventa endpoint

        Expected results:
            * response status code equals to 200
        """
        response = requests.get(url=f"http://{HOST}:{PORT}/casas/preventa")

        self.assertEqual(
            response.status_code,
            200,
            f"Expected status code 200 but got {response.status_code}",
        )

    def test_casas_preventa_content_response(self):
        """
        Test:
            * /casas/preventa endpoint

        Expected results:
            * content response only contents casas with status equal to
            pre_venta
        """
        response = requests.get(url=f"http://{HOST}:{PORT}/casas/preventa")

        data = response.json()
        for casa in data:
            self.assertEqual(
                casa["status"],
                "pre_venta",
                f"Expected status 'pre_venta' but got {casa['status']}",
            )

    def test_casas_preventa_content_response_city_and_addres_not_null(self):
        """
        Test:
            * /casas/preventa endpoint

        Expected results:
            * content response only contents casas with non empty address and
            city
        """
        response = requests.get(url=f"http://{HOST}:{PORT}/casas/preventa")

        data = response.json()
        for casa in data:
            self.assertNotIn(
                casa["address"],
                ("", None),
                "Expected address not empty but it's empty",
            )
            self.assertNotIn(
                casa["city"],
                ("", None),
                "Expected city not empty but it's empty",
            )

    def test_casas_preventa_year_filter(self):
        """
        Test:
            * /casas/preventa endpoint

        Expected results:
            * content response only contents with filter by year condition
        """
        year = 2020
        response = requests.get(
            url=f"http://{HOST}:{PORT}/casas/preventa", params={"year": year}
        )

        data = response.json()
        for casa in data:
            self.assertEqual(
                casa["year"],
                year,
                f"Expected year {year} but got {casa['year']}",
            )

    def test_casas_preventa_year_and_city_filter(self):
        """
        Test:
            * /casas/preventa endpoint

        Expected results:
            * content response only contents with filter by year condition
        """
        year = 2002
        city = "medellin"
        response = requests.get(
            url=f"http://{HOST}:{PORT}/casas/preventa",
            params={"year": year, "city": city},
        )

        data = response.json()
        for casa in data:
            self.assertEqual(
                casa["year"],
                year,
                f"Expected year {year} but got {casa['year']}",
            )
            self.assertEqual(
                casa["city"],
                city,
                f"Expected year {city} but got {casa['city']}",
            )

    def test_casas_preventa_status_code_204(self):
        """
        Test:
            * /casas/preventa endpoint with not valid filter

        Expected results:
            * response status code equals to 200
        """
        response = requests.get(
            url=f"http://{HOST}:{PORT}/casas/preventa", params={"foo": "bar"}
        )

        self.assertEqual(
            response.status_code,
            204,
            f"Expected status code 200 but got {response.status_code}",
        )

    def test_casas_enventa_status_code_200(self):
        """
        Test:
            * /casas/enventa endpoint

        Expected results:
            * response status code equals to 200
        """
        response = requests.get(url=f"http://{HOST}:{PORT}/casas/enventa")

        self.assertEqual(
            response.status_code,
            200,
            f"Expected status code 200 but got {response.status_code}",
        )

    def test_casas_enventa_content_response(self):
        """
        Test:
            * /casas/enventa endpoint

        Expected results:
            * content response only contents casas with status equal to
            en_venta
        """
        response = requests.get(url=f"http://{HOST}:{PORT}/casas/enventa")

        data = response.json()
        for casa in data:
            self.assertEqual(
                casa["status"],
                "en_venta",
                f"Expected status 'en_venta' but got {casa['status']}",
            )

    def test_casas_enventa_content_response_city_and_addres_not_null(self):
        """
        Test:
            * /casas/enventa endpoint

        Expected results:
            * content response only contents casas with non empty address and
            city
        """
        response = requests.get(url=f"http://{HOST}:{PORT}/casas/enventa")

        data = response.json()
        for casa in data:
            self.assertNotIn(
                casa["address"],
                ("", None),
                "Expected address not empty but it's empty",
            )
            self.assertNotIn(
                casa["city"],
                ("", None),
                "Expected city not empty but it's empty",
            )

    def test_casas_enventa_year_filter(self):
        """
        Test:
            * /casas/enventa endpoint

        Expected results:
            * content response only contents with filter by year condition
        """
        year = 2011
        response = requests.get(
            url=f"http://{HOST}:{PORT}/casas/enventa", params={"year": year}
        )

        data = response.json()
        for casa in data:
            self.assertEqual(
                casa["year"],
                year,
                f"Expected year {year} but got {casa['year']}",
            )

    def test_casas_enventa_year_and_city_filter(self):
        """
        Test:
            * /casas/enventa endpoint

        Expected results:
            * content response only contents with filter by year condition
        """
        year = 2011
        city = "medellin"
        response = requests.get(
            url=f"http://{HOST}:{PORT}/casas/enventa",
            params={"year": year, "city": city},
        )

        data = response.json()
        for casa in data:
            self.assertEqual(
                casa["year"],
                year,
                f"Expected year {year} but got {casa['year']}",
            )
            self.assertEqual(
                casa["city"],
                city,
                f"Expected year {city} but got {casa['city']}",
            )

    def test_casas_enventa_status_code_204(self):
        """
        Test:
            * /casas/enventa endpoint with not valid filter

        Expected results:
            * response status code equals to 200
        """
        response = requests.get(
            url=f"http://{HOST}:{PORT}/casas/enventa", params={"foo": "bar"}
        )

        self.assertEqual(
            response.status_code,
            204,
            f"Expected status code 200 but got {response.status_code}",
        )

    def test_casas_vendido_status_code_200(self):
        """
        Test:
            * /casas/vendido endpoint

        Expected results:
            * response status code equals to 200
        """
        response = requests.get(url=f"http://{HOST}:{PORT}/casas/vendido")

        self.assertEqual(
            response.status_code,
            200,
            f"Expected status code 200 but got {response.status_code}",
        )

    def test_casas_vendido_content_response(self):
        """
        Test:
            * /casas/vendido endpoint

        Expected results:
            * content response only contents casas with status equal to
            en_venta
        """
        response = requests.get(url=f"http://{HOST}:{PORT}/casas/vendido")

        data = response.json()
        for casa in data:
            self.assertEqual(
                casa["status"],
                "vendido",
                f"Expected status 'vendido' but got {casa['status']}",
            )

    def test_casas_vendido_content_response_city_and_addres_not_null(self):
        """
        Test:
            * /casas/vendido endpoint

        Expected results:
            * content response only contents casas with non empty address and
            city
        """
        response = requests.get(url=f"http://{HOST}:{PORT}/casas/vendido")

        data = response.json()
        for casa in data:
            self.assertNotIn(
                casa["address"],
                ("", None),
                "Expected address not empty but it's empty",
            )
            self.assertNotIn(
                casa["city"],
                ("", None),
                "Expected city not empty but it's empty",
            )

    def test_casas_vendido_year_filter(self):
        """
        Test:
            * /casas/vendido endpoint

        Expected results:
            * content response only contents with filter by year condition
        """
        year = 2020
        response = requests.get(
            url=f"http://{HOST}:{PORT}/casas/vendido", params={"year": year}
        )

        data = response.json()
        for casa in data:
            self.assertEqual(
                casa["year"],
                year,
                f"Expected year {year} but got {casa['year']}",
            )

    def test_casas_vendido_year_and_city_filter(self):
        """
        Test:
            * /casas/vendido endpoint

        Expected results:
            * content response only contents with filter by year condition
        """
        year = 2020
        city = "pereira"
        response = requests.get(
            url=f"http://{HOST}:{PORT}/casas/vendido",
            params={"year": year, "city": city},
        )

        data = response.json()
        for casa in data:
            self.assertEqual(
                casa["year"],
                year,
                f"Expected year {year} but got {casa['year']}",
            )
            self.assertEqual(
                casa["city"],
                city,
                f"Expected year {city} but got {casa['city']}",
            )

    def test_casas_vendido_status_code_204(self):
        """
        Test:
            * /casas/vendido endpoint with not valid filter

        Expected results:
            * response status code equals to 200
        """
        response = requests.get(
            url=f"http://{HOST}:{PORT}/casas/vendido", params={"foo": "bar"}
        )

        self.assertEqual(
            response.status_code,
            204,
            f"Expected status code 200 but got {response.status_code}",
        )
