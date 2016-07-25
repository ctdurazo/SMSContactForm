<?php
/**
 * Created by PhpStorm.
 * User: christian durazo
 * Date: 5/5/16
 * Time: 10:20 AM
 */

require_once "Mail.php";

//check if required fields are set
if (isset($_REQUEST['submit'])) {
    if (isset($_REQUEST['Name'])) {
        $name = $_REQUEST['Name'];
    }
    if (isset($_REQUEST['Phone'])) {
        $phone = $_REQUEST['Phone'];
    }
    if (isset($_REQUEST['Service'])) {
        $service = $_REQUEST['Service'];
    }
    if (isset($_REQUEST['time'])) {
        $time = $_REQUEST['time'];
    }
    if (isset($_REQUEST['datepicker'])) {
        $date = $_REQUEST['datepicker'];
    }else{
        date_default_timezone_set('America/Los_Angeles');
        $date = date('m/d/Y', time());
    }


    //create mail form
    $from = "<address@email.com>"; //replace with your email host
    $to = "<number@host.com>";     //replace with your SMS email, i.e. xxxxxxxxxx@vtext.com for verizon
    $subject = 'Message from a site visitor ' . $name;

    $body = 'From: ' . $name . "\n";
    $body .= 'Phone: ' . $phone . "\n";

    //check if email is set and add to the mail form
    if (isset($_REQUEST['Email'])) {
        $email = $_REQUEST['Email'];
        $body .= 'E-mail: ' . $email . "\n";
    }

    $body .= 'Service: ' . $service ."\n";

    $body .= 'Time: ' . $time ."\n";

    $body .= 'Date: ' . $date ."\n";

    //check if trainer is set and add to the mail form
    if(isset($_REQUEST['Trainer'])) {
        $trainer = $_REQUEST['Trainer'];
        $body .= 'Trainer: ' . $trainer . "\n";
    }

    //check if message is set and add to the mail form
    if (isset($_REQUEST['Message'])) {
        $message = $_REQUEST['Message'];
        $body .= 'Additional Information: ' . $message;

    }

    //smtp authentication
    $host = "smtp.gmail.com";        //use your smtp host for your email host
    $username = "address@email.com"; //use your email host username
    $password = "userpassword";      //use your email host password

    $headers = array('From' => $from,
        'To' => $to,
        'Subject' => $subject);

    $smtp = Mail::factory('smtp',
        array('host' => $host,
            'auth' => true,
            'username' => $username,
            'password' => $password));

    //send mail 
    $mail = $smtp->send($to, $headers, $body);
    if (PEAR::isError($mail)) {
        echo("<p>Message could not be sent due to an error: " . $mail->getMessage() . "</p>");
    } else {
        echo("<p>Message successfully sent!</p>");
    }
} else{
    echo("<p>Message could not be sent due to an error.<p>");
}
?>

