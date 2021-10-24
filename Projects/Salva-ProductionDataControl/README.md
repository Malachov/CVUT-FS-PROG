# Production data control

This project is application that control output data from production lines. If defined values exceed defined threshold, it will send alert email.

Application consist of two parts. Service (daemon) running on local computer where lines stands and from web application that collects historical data, evaluate defined metrics and eventually send alert emails.