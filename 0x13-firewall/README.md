# Firewall
0. Block all incoming traffic but:
<p>Let’s install the <code>ufw</code> firewall and setup a few rules on <code>web-01</code>.</p>
<p>Requirements:</p>
<ul>
<li>The requirements below must be applied to <code>web-01</code> (feel free to do it on <code>lb-01</code> and <code>web-02</code>, but it won’t be checked)</li>
<li>Configure <code>ufw</code> so that it blocks all incoming traffic, except the following TCP ports:

<ul>
<li><code>22</code> (SSH)</li>
<li><code>443</code> (HTTPS SSL)</li>
<li><code>80</code> (HTTP)</li>
</ul></li>
<li>Share the <code>ufw</code> commands that you used in your answer file</li>
</ul>