<?php
session_start();
if(empty($_SESSION['login'])){
	echo 'no login';
}else{
	echo 'ok ,you login ';
}
