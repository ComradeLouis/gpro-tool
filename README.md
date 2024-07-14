README

Yeah this is based on the GPRO api - found here https://api.gpro.net.

Will be incrementally updated to use all calls from here, and then create a tool that will allow you to generate setups/run practice.

To use this yourself - create the API token as explained on above website (through GPRO app), then after downloading create a .env file, and paste the token in there in the form 'token' = "{token}". This will allow it to be used by you, and will then work as expected (theoretically!)

-- Added 13/07 - part wear calcs per CT risk chosen (steps of 10)

-- Added 14/07 - TCD calculation and time loss from tyres/fuel/stops

To be added - strategy calculations (time loss from tyre choice, fuel load, time per added stop etc). These will output an optimum strategy per ct risk