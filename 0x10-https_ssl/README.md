# HTTPS SSL
0. <p>Configure your domain zone so that the subdomain <code>www</code> points to your load-balancer IP (<code>lb-01</code>).
Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.</p>
<p>Requirements:</p>
<ul>
<li>Add the subdomain <code>www</code> to your domain, point it to your <code>lb-01</code> IP (your domain name might  be configured with default subdomains, feel free to remove them)</li>
<li>Add the subdomain <code>lb-01</code> to your domain, point it to your <code>lb-01</code> IP</li>
<li>Add the subdomain <code>web-01</code> to your domain, point it to your <code>web-01</code> IP</li>
<li>Add the subdomain <code>web-02</code> to your domain, point it to your <code>web-02</code> IP</li>
<li>Your Bash script must accept 2 arguments:

<ol>
<li><code>domain</code>:

<ul>
<li> type: string</li>
<li> what: domain name to audit</li>
<li>mandatory: yes</li>
</ul></li>
<li><code>subdomain</code>:

<ul>
<li>type: string</li>
<li>what: specific subdomain to audit</li>
<li>mandatory: no</li>
</ul></li>
</ol></li>
<li>Output:  <code>The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]</code></li>
<li>When only the parameter <code>domain</code> is provided, display information for its subdomains <code>www</code>, <code>lb-01</code>, <code>web-01</code> and <code>web-02</code> - in this specific order</li>
<li>When passing <code>domain</code> and <code>subdomain</code> parameters, display information for the specified subdomain</li>
<li>Ignore <code>shellcheck</code> case <code>SC2086</code></li>
<li>Must use: 

<ul>
<li><code>awk</code></li>
<li>at least one Bash function</li>
</ul></li>
<li>You do not need to handle edge cases such as:

<ul>
<li>Empty parameters </li>
<li>Nonexistent domain names</li>
<li>Nonexistent subdomains</li>
</ul></li>
</ul>