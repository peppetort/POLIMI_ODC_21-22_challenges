<?php
include 'base.php';
?>

<h1>Welcome to Itemizer</h1>


  <form enctype="multipart/form-data" action="/create_item.php" method="post">
  <div style="margin: 32px; display: flex; justify-content: center">
    <p style="margin: 0">Item Name:&nbsp</p>
    <input type="text"
           id="name" name="name">
    <br/>
    <p style="margin: 0">Description:&nbsp</p>
    <input type="textarea"
           id="description" name="description">
    <br/>
    <p style="margin: 0">Value:&nbsp</p>
    <input type="text"
           id="value" name="value">
    <br/>
  </div>
  <div style="margin: 32px; justify-content: center">
    <button class="btn" id="create_item">Create Item</button>
  </div>
  </form>


  <?php
if (isset($_POST['name'])) {
  if(isset($_SESSION["user"])){

    $db = new DB();
    $name = $_POST['name'];
    $desc = $_POST['description'];
    $value = $_POST['value'];

    if (empty($name)) { echo("Item Name is required"); die(); }
    if (empty($desc)) { echo("Description is required"); die(); }
    if (empty($value)) { echo("Value is required"); die(); }
    $item = Item::generate_item($name, $desc, $value);
    $item_id = $item->fid;
    $_SESSION["user"]->addItem($item_id);
    echo " New Item: ".$item;
  }
}
  ?>


<?php
include 'footer.php';
?>