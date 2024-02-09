# BACnet dump tool

This tool is used to discover properties on a bacnet device.

# How to run it?

Start with creating a virtual environment:

    python3 -m venv venv

Activate the virtual environment:

    source venv/bin/activate

Install the requirements:

    pip install -r requirements.txt

Run the tool:

    python3 main.py <deviceIPAddress>

To save the output to a file:

    python3 main.py <deviceIPAddress> > output.jsonl