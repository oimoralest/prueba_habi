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
        sleep(1)

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
        response = requests.get(f"http://{HOST}:{PORT}/casas/preventa")

        self.assertEqual(
            response.status_code,
            200,
            f"Expected status code 200 but got {response.status_code}",
        )
