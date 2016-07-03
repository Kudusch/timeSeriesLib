# timeSeriesLib

This tool converts case based .csv data to data more fitting for time series analysis.

## Usage

`python controler.py [YOUR DATA].csv [OPTIONS].txt`

The data must be a csv-file, with either `,`or `;` as delimiter.

The `options.txt` must contain the following parameters:

- Start: The variable containing the beginning of the case
- Ende: The variable containing the end of the case
- Trennungszeichen: The delimieter used for input and output csv
- Dauer: The length of the time series in seconds

… and one or more of the following parameters:

- Variable: The variable to convert
- Werte: The expected values of the variable

For an example `options.txt` see (Eingabe.txt)[Eingabe.txt]
