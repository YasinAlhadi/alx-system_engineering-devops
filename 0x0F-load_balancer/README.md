# Load balancer
0. Double the number of webservers.<br />

Requirements:<br />

Configure Nginx so that its HTTP response contains a custom header (on web-01 and web-02)<br />
The name of the custom HTTP header must be X-Served-By.<br />
The value of the custom HTTP header must be the hostname of the server Nginx is running on.<br />
Write 0-custom_http_response_header so that it configures a brand new Ubuntu machine to the requirements asked in this task.<br />
Ignore SC2154 for shellcheck

1. Install and configure HAproxy on your lb-01 server.<br />

Requirements:<br />

Configure HAproxy so that it send traffic to web-01 and web-02.<br />
Distribute requests using a roundrobin algorithm.<br />
Make sure that HAproxy can be managed via an init script.<br />
Make sure that your servers are configured with the right hostnames: [STUDENT_ID]-web-01 and [STUDENT_ID]-web-02. If not, follow this tutorial.<br />
For your answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements.
