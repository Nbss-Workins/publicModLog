<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" href="bootstrap.css" />
  <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/v/dt/jq-3.3.1/dt-1.10.21/datatables.min.css"/>
  <script type="text/javascript" src="https://cdn.datatables.net/v/dt/jq-3.3.1/dt-1.10.21/datatables.min.js" defer></script>
  <script src="jquery.js"></script>
  <title>Mod logs</title>
</head>
<body>
<table class="table" id="table">
<thead>
<tr>
<th>Date</th>
<th>Mod</th>
<th>Action</th>
<th>Details</th>
</tr>
</thead>
<tbody>
<?php
$conn = mysqli_connect("localhost", "YOUR_USER_HERE", "YOUR_PASSWORD", "redditModLogs");			#Change this
// Check connection
if ($conn->connect_error) {
die("Connection failed: " . $conn->connect_error);
}
$sql = "SELECT actDate, author, action, details FROM modlogs";
$result = $conn->query($sql);
if ($result->num_rows > 0) {
// output data of each row
while($row = $result->fetch_assoc()) {
echo "<tr><td>" . $row["actDate"]. "</td><td>" . $row["author"] . "</td><td>"
. $row["action"]. "</td><td>" . $row["details"] . "</td></tr>";
}
echo "</table>";
} else { echo "0 results"; }
$conn->close();
?>
</tbody>
</table>
<script type="text/javascript">
    $(document).ready( function () {
    $('#table').DataTable();
} );
</script>
</body>
</html>