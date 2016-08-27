<?php
namespace Mytest\Controller;
use Think\Controller;

class FormController extends Controller{
    public function a(){
	var_dump( I('path.3/b','asdf','') );
    }
    public function insert(){
	$Form=D('data');
	if($Form->create()){
	    $result=$Form->add();
	    if($result){
		$this->success('ok');
	    }else{
		$this->error('wrong');
	    }
	}else{
	    $this->error($Form->getError());
	}
    }

    public function read($id=1){
	$Data=M('data');
	//$result=$Data->find($id);
	$result=$Data->where('id=3')->getField('data');
	if($result){
	    $this->assign('name',$result);
	}else{
	    $this->error('wrong data');
	}
	$this->display();
    }

    public function edit($id=1){
	$Data=M('Data');
	$result=$Data->find($id);
var_dump($result);
	if($result){
	    $this->assign('name',$result);
	    $this->display();
	}else{
	    $this->error('wrong read');
	}
    }
    
    public function update(){
	$Data=M('data');
	if($Data->create()){
	    $result=$Data->save();
	    if($result){
		$this->success('updated ok');
	    }else{
		$this->error('updated failed');
	    }
	}else{
	    $this->error($Data->getError());
	}
    }
	    

}
