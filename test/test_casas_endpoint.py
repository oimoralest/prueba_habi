import subprocess
import unittest
from time import sleep

import requests

from enums import HOST, PORT


class CasasEndpointTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.server = subprocess.Popen(["python3", "main.py"])

        # Needed so server can open the port for requests
        sleep(3)

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
