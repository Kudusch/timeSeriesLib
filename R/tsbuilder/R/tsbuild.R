#' Build a time-series object from case-based data.
#'
#' @param df A data frame.
#' @param TSstart Time stamp.
#' @param TSstop Time stamp.
#' @param values Values to aggregate.
#' @param TSformat A string containing the TS format. Defaults to "YYYY-MM-DD HH:MM:SS"
#' @return A time-series object based on \code{df}.
#' @examples
#' tsbuild(df)
tsbuild <- function(df, TSstart, TSstop = TSstart, values, TSformat = "YYYY-MM-DD HH:MM:SS") {
  # generate empty time series

  # for each row in df
  # get time stamp or intervall & value
  # add to row(s) in ts-df
  TSstart <- eval(substitute(TSstart),df, parent.frame())
  TSstart <- strptime(TSstart,TSformat)
  TSstop <- eval(substitute(TSstop),df, parent.frame())
  TSstop <- strptime(TSstop,TSformat)
  dur <- as.numeric(TSstop-TSstart, units="secs")+1
  TSdata <- data.frame(TSstart,TSstop,dur)

  max <- sort(unique(TSdata$TSstop), decreasing = T)[1]
  min <- sort(unique(TSdata$TSstart))[1]
  len <- as.numeric(max-min, units="secs")
  TSout <- data.frame(seq(1,len))
  names(TSout)[1] <- "n"
  for (value in values) {
    valueList <- sort(as.character(unique(df[[value]])))
    TSdata[[value]] <- df[[value]]
    for (v in valueList) {
      TSout[[paste(value, v, sep = '_')]] <- 0
    }
  }

  for(n in 1:nrow(TSdata)) {
    for(v in 4:ncol(TSdata)) {
      for (t in 1:TSdata[n,3]) {
        TSout[paste(names(TSdata)[v], as.character(TSdata[n,v]), sep = '_'),as.numeric((TSdata$TSstart[4])-min, units="secs")] <- (TSout[paste(names(TSdata)[v], as.character(TSdata[n,v]), sep = '_'),as.numeric((TSdata$TSstart[4])-min, units="secs")])+1
      }
      #do something to the data
    }
  }
  return(TSout)
}
