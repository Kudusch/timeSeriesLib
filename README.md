# timeSeriesLib

This tool converts case based .csv data to data more fitting for time series analysis.

## Usage

`python timeSeries/timeSeries.py [OPTIONS] [YOUR DATA].csv`

The data must be a csv-file, with either `,`or `;` as delimiter.

The options file must contain the following parameters:

- Start: The variable containing the beginning of the case
- End: The variable containing the end of the case
- Delimiter: The delimieter used for input and output csv
- Duration: The length of the time series in seconds
- Cumulate to: Either *None* or the number of seconds to cumulate

… and one or more of the following parameters:

- Variable: The variable to convert
- Values: The expected values of the variable

For an example options file see [Example options.txt](/example/Example options.txt)
