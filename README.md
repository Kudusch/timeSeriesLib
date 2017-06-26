# timeSeriesLib

This tool converts case based .csv data to data more fitting for time series analysis.

## Usage

`python timeSeries/timeSeries.py [MODE] [OPTIONS] [DATA]`

### [MODE]

Choose `-1` for data with a start and stop variable and `-2` for data, which has a variable for every point in the time series.

### [OPTIONS]

The options file must contain the following parameters:

#### In mode 1:

- Start: The variable containing the beginning of the case
- End: The variable containing the end of the case
- Delimiter: The delimieter used for input and output csv
- Duration: The length of the time series in seconds
- Cumulate to: Either *None* or the number of seconds to cumulate

… and one or more of the following parameters:

- Variable: The variable to convert
- Values: The expected values of the variable

#### In mode 2:

- Delimiter: The delimieter used for input and output csv
- Values: The expected values of the variable

### [DATA]

The data must be a csv-file, with either `,` or `;` as delimiter.

For an example options file see [Example options.txt](/example/Example options.txt)
