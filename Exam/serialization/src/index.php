<?php
include 'base.php';
?>

<h1>Welcome to Itemizer</h1>

<?php

if(isset($_SESSION["user"])){

    foreach ($_SESSION["user"]->items as &$c) {
        printf("%s", new Item($c));
    }

}
?>


<?php
include 'footer.php';
?>