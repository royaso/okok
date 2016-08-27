<?php
session_start();
$name=$_POST['name'];
$passwd=$_POST['passwd'];
if ($name =='name' && $passwd == 'passwd' ) {
	$_SESSION['login']=1;
	echo 'ok, go to 2.php';
}else{
	echo 'wrong passwd or name combination';
}
