# Temperature Probe Correlation Tool

## Background

The need for this script came about when I repurposed an old bluetooth BBQ thermometer I had laying around. 

The BBQ thermometer (Inkbird IBT-2X) came with two standard "meat probes". I modified it by chopping off one of the meat probes and soldering a small 10K thermistor in place. This allows me to attach to various electronics and read the temperatures using the app on my phone. Very handy!

However, the temperature read by the new thermistor is different than the original probes. It seems to read about 74-79 degrees F higher than the original probes do.

So, I began calibrating the thermistor temperatures to probe temperatures by starting with hot water, then reading the values of both probes and adding colder water to get some data to start with.

I entered those measurements into Excel and noticed a linear correlation between the values:

```
Probe	  Thermistor	Ratio (Thermistor/Probe)
151	    230	        1.52317
120	    196	        1.63333
117	    194	        1.65811
106	    181	        1.70754
95	    169	        1.77894
86	    160	        1.86046
81	    154	        1.90123
77	    151	        1.96103
75	    149         1.98666
```

Looking at the data, I can see a clear pattern to the ratio of Thermistor values divided by the Probe values. With that in mind, I set out to create a script that could fill in the blanks, and provide me with a usable chart for each value. With that in hand, I can easily reference the real temperature read by the thermistor.

After some time with GPT-4, the resulting script does exactly that. Given an input of measured data points, the script will extrapolate all of the values in between and provide a readable chart to reference the real temperatures read by the thermistor.

Since I prefer to read the temperatures in Celsius, I added a conversion to Celsius. This allows me to leave the thermometer on the Fahrenheit setting which allows for finer-grained readings, which I can then easily convert to real Celsius values with my newly created chart.

## Features

- Uses linear regression to extrapolate missing values
- Easily editable data input
- Option to specify the range for extrapolation
- Fahrenheit to Celsius conversion (optional)

## Usage

1. Edit the `data` variable to include your known data points. Format is: (Probe, Thermistor).
2. Adjust the `lowest_value_to_extrapolate` and `highest_value_to_extrapolate` variables to define the range for extrapolation.
3. Set the `convert_to_celsius` flag to `True` or `False` to enable or disable the conversion of probe values to Celsius.
4. Run the script to print the table of values.

## Example Output

```
Probe      Thermistor   Celsius   
60         132          15.6
61         133          16.1
62         134          16.7
```


## Dependencies

- `scikit-learn`: Required for linear regression.

## Installation

You can install the required dependencies using pip:

```bash
pip install scikit-learn
```

## License

This project is available under the MIT License. Feel free to use, modify, and distribute the code as you see fit.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the issues page or send a pull request.
