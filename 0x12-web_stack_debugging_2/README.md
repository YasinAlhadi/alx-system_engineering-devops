# Web stack debugging 2
0. Run software as another user<br />

<p>The user <code>root</code> is, on Linux, the “superuser”. It can do anything it wants, that’s a good and bad thing. A good practice is that one should never be logged in the <code>root</code> user, as if you fat finger a command and for example run <code>rm -rf /</code>, there is no comeback. That’s why it is preferable to run as a privileged user, meaning that the user also has the ability to perform tasks that the <code>root</code> user can do, just need to use a specific command that you need to discover.</p>
<p>For the containers that you are given in this project as well as the checker, everything is run under the <code>root</code> user, which has the ability to run anything as another user.</p>
<p>Requirements:</p>
<ul>
<li>write a Bash script that accepts one argument</li>
<li>the script should run the <code>whoami</code> command under the user passed as an argument</li>
<li>make sure to try your script by passing different users</li>
</ul>