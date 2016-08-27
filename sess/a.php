<?php
session_start();
if (empty($_SESSION['login'])){
	
?>
<form action='login.php' method='post'>
name <input type="text" name='name'><br>
passwd <input type="password" name='passwd'><br>
<input type="submit" value="click">

</form>

<?php
}else{
	echo 'you already login';
}
