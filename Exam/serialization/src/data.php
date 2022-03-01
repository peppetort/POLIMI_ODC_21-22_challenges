<?php
// ini_set('display_errors', 1);
// ini_set('display_startup_errors', 1);
// error_reporting(E_ALL);
// error_reporting(0);

class User{
  public $name;
  public $fid;
  public $items;

  function __construct($fid, $name){
    $this->id = $fid;
    $this->name = $name;
    $this->items = array(); 
  }

  public function addItem($fid){
    array_push($this->items, $fid);
  }

}

class Item{
  public $fid;
  public $name;
  public $description;
  public $value;

  function __construct($fid){
    $f = fopen("./items/".$fid, "r");
    $this->name = fgets($f);
    $this->description = fgets($f);
    $this->value = fgets($f);
    $this->fid = $fid;
  }

  static public function generate_item($name, $description, $value){
    $fid = rand();
    $f = fopen("./items/".$fid, "w");
    fwrite($f, $name."\n");
    fwrite($f, $description."\n");
    fwrite($f, $value."\n");
    return new Item($fid);
  }

  function __toString(){
    return "<div> <h2>".$this->name."</h2> <p>".$this->description."</p> <span>".$this->value."</span> </div>";
  }
}
?>