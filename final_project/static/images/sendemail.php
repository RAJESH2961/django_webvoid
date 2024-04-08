<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Collect form data
    $name = $_POST['name'];
    $email = $_POST['email'];
    $subject = $_POST['subject'];
    $message = $_POST['message'];

    // Send email
    $to = "grajesh2906@gmail.com"; // Replace with your email address
    $headers = "From: $name <$email>";
    $body = "Subject: $subject\n\nMessage: $message";
    if (mail($to, $subject, $body, $headers)) {
        echo "Email sent successfully";
    } else {
        echo "Failed to send email";
    }
}
?>
