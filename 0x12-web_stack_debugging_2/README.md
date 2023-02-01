# Web stack debugging 2
0. Run software as another user<br />
<p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/eaeff07a715ff880b1ceb8e863a1d141a74a7f85.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230131%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20230131T094651Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=8997088fa3f07c375fcebf2be46255ca324ae1cdbe3dd573b3ee31d946e4625f" alt="" loading="lazy" style=""></p>
<p>The user <code>root</code> is, on Linux, the “superuser”. It can do anything it wants, that’s a good and bad thing. A good practice is that one should never be logged in the <code>root</code> user, as if you fat finger a command and for example run <code>rm -rf /</code>, there is no comeback. That’s why it is preferable to run as a privileged user, meaning that the user also has the ability to perform tasks that the <code>root</code> user can do, just need to use a specific command that you need to discover.</p>
<p>For the containers that you are given in this project as well as the checker, everything is run under the <code>root</code> user, which has the ability to run anything as another user.</p>
<p>Requirements:</p>
<ul>
<li>write a Bash script that accepts one argument</li>
<li>the script should run the <code>whoami</code> command under the user passed as an argument</li>
<li>make sure to try your script by passing different users</li>
</ul>