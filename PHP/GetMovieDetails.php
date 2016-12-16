<!DOCTYPE html>
<html>
<head>
  <title>MovieSort</title>
  <link rel="stylesheet" href="css/bootstrap.css" />
  <link rel="stylesheet" href="line.css" />
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  <link href="https://fonts.googleapis.com/css?family=Bungee+Inline" rel="stylesheet">

  <style>
  a{
    color:black;
  }
  a:hover {
    color:blue;
  }
  </style>
</head>

 <?php
 $errno = NULL;
 $errstr = NULL;
if ( @fopen("https://www.google.com", "r") )
{
  //error handler function
  function customError($errno, $errstr) {
    $log = fopen("errorlog.txt", "w") or die("Unable to open file!");
    $error = "<b>Error:</b> [$errno] $errstr";
    fwrite($log, $error);
    fclose($log);
  }

  //set error handler
  set_error_handler("customError");

?>

<body background="cinemag.jpg">
<?php
// define variables and set to empty values
$path = $list1 = "";
$req1 = array();
$movienrating1 = array();
//Err
$pathErr = $list1Err = "";
$sdir = $_GET["link"];
echo "blblblb".$sdir."<br>";
//name

function test_input($data) {
   $data = trim($data);
   $data = stripslashes($data);
   $data = htmlspecialchars($data);
   return $data;
}
?>

<div class="container-fluid">
<div class="row">
  <div class="col-sm-12">
<center><h1 style='color:white;font-size:90px;font-family:Bungee Inline, cursive;'>MovieSort</h1></center>
</div>
</div>
</div>

<div class="container-fluid">


          <center>
          <h1> The List </h1>
          </center>
        <div class="jumbotron">
          <center>
        <table id="test" border="1" style="margin-left:12px;margin-right:12px;">

         <tr>
           <th>Rating</th>
           <th>Name</th>
           <th>Genre</th>
           <th>Director</th>
           <th>Writer</th>
           <th>Cast</th>
           <th>Description</th>
           <th>Release Date</th>
         </tr>


        <?php ob_start();

        // Open the directory, and read its contents

        //$unwant = array(".srt",".txt");

        function listFolderFiles($dir){
          if (is_dir($dir)) {
            $files = scandir($dir);
            foreach($files as $file){
                if($file != '.' && $file != '..'){
                    if(is_dir($dir.'/'.$file)){
                    if(is_dir($dir.'/'.$file)) listFolderFiles($dir.'/'.$file);
                  }
                    else {
                      $ext = array(".avi",".mp4","m4v","mkv");
                      //echo $file;
                      $filename = $file;
                      foreach ($ext as &$value1){
                        if (strpos($file, $value1) == true) {

                          $replace = array("DvD","TamilRockers","AVC","PROPER.DVDRip.XViD.CD1-DVL","PROPER.DVDRip","E SuB xRG","m4v","mp4","CD2","CD1","DVL","torentz","Stealthmaster","SCRGooN"," Mafiaking","M2Tv","cc ","SCRT0XiCiNK","3xforum",".avi","1.4","5.1","-","DVDRip","BRRip","XviD","1CDRip","aXXo","[","]","(",")","{","}","{{","}}",
                          "x264","720p","DvDScr","MP3","HDRip","WebRip","ETRG","YIFY","StyLishSaLH","StyLish Release","TrippleAudio",
                                  "EngHindiIndonesian","385MB","CooL GuY","a2zRG","x264","Hindi","AAC","AC3","MP3"," R6","HDRip","H264","ESub","AQOS",
                                  "ALLiANCE","UNRATED","ExtraTorrentRG","BrRip","mkv","mpg","DiAMOND","UsaBitcom","AMIABLE","BRRIP","XVID","AbSurdiTy",
                                  "DVDRiP","TASTE","BluRay","HR","COCAIN","_",".","BestDivX","MAXSPEED","Eng","500MB","FXG","Ac3","Feel","Subs","S4A","BDRip","FTW","Xvid","Noir","1337x","ReVoTT",
                                  "GlowGaze","mp4","Unrated","hdrip","ARCHiViST","TheWretched","www","torrentfive","com","1080p","1080","SecretMyth","Kingdom","Release","RISES","DvDrip","ViP3R","RISES","BiDA","READNFO",
                                  "HELLRAZ0R","tots","BeStDivX","UsaBit","FASM","NeroZ","576p","LiMiTED","Series","ExtraTorrent","DVDRIP","~",
                                  "BRRiP","699MB","700MB","greenbud","B89","480p","AMX","007","DVDrip","h264","phrax","ENG","TODE","LiNE",
                                  "XVid","sC0rp","PTpower","OSCARS","DXVA","MXMG","3LT0N","TiTAN","4PlayHD","HQ","HDRiP","MoH","MP4","BadMeetsEvil",
                                  "XViD","3Li","PTpOWeR","3D","HSBS","CC","RiPS","WEBRip","R5","PSiG","'GokU61","GB","GokU61","NL","EE","Rel","NL",
                                  "PSEUDO","DVD","Rip","NeRoZ","EXTENDED","DVDScr","xvid","WarrLord","SCREAM","MERRY","XMAS","iMB","7o9",
                                  "Exclusive","171","DiDee","v2","Scr","SaM","MOV","BRrip","CharmeLeon","Silver RG","1xCD","DDR","1CD","X264","ExtraTorrenRG",
                              "Srkfan","UNiQUE","Dvd","crazy torrent","Spidy","PRiSTiNE","HD","Ganool","TS","BiTo","ARiGOLD","rip","Rets","teh","ChivveZ","song4",
                              "playXD","LIMITED","600MB","700MB","900MB");

                    /* check for differences with above later
                    $replace = array("TamilRockers","AVC","PROPER.DVDRip.XViD.CD1-DVL","PROPER.DVDRip","E SuB xRG","m4v","mp4","CD2","CD1","DVL","torentz","3xforum",".avi","1.4","5.1","-","DVDRip","BRRip","XviD","1CDRip","aXXo","[","]","(",")","{","}","{{","}}",
                      "x264","720p","DvDScr","MP3","HDRip","WebRip","ETRG","YIFY","StyLishSaLH","StyLish Release","TrippleAudio",
                              "EngHindiIndonesian","385MB","CooL GuY","a2zRG","x264","Hindi","AAC","AC3","MP3"," R6","HDRip","H264","ESub","AQOS",
                              "ALLiANCE","UNRATED","ExtraTorrentRG","BrRip","mkv","mpg","DiAMOND","UsaBitcom","AMIABLE","BRRIP","XVID","AbSurdiTy",
                              "DVDRiP","TASTE","BluRay","HR","COCAIN","_",".","BestDivX","MAXSPEED","Eng","500MB","FXG","Ac3","Feel","Subs","S4A","BDRip","FTW","Xvid","Noir","1337x","ReVoTT",
                              "GlowGaze","mp4","Unrated","hdrip","ARCHiViST","TheWretched","www","torrentfive","com","1080p","1080","SecretMyth","Kingdom","Release","RISES","DvDrip","ViP3R","RISES","BiDA","READNFO",
                              "HELLRAZ0R","tots","BeStDivX","UsaBit","FASM","NeroZ","576p","LiMiTED","Series","ExtraTorrent","DVDRIP","~",
                              "BRRiP","699MB","700MB","greenbud","B89","480p","AMX","007","DVDrip","h264","phrax","ENG","TODE","LiNE",
                              "XVid","sC0rp","PTpower","OSCARS","DXVA","MXMG","3LT0N","TiTAN","4PlayHD","HQ","HDRiP","MoH","MP4","BadMeetsEvil",
                              "XViD","3Li","PTpOWeR","3D","HSBS","CC","RiPS","WEBRip","R5","PSiG","'GokU61","GB","GokU61","NL","EE","Rel","NL",
                              "PSEUDO","DVD","Rip","NeRoZ","EXTENDED","DVDScr","xvid","WarrLord","SCREAM","MERRY","XMAS","iMB","7o9",
                              "Exclusive","171","DiDee","v2","Scr","SaM","MOV","BRrip","CharmeLeon","Silver RG","1xCD","DDR","1CD","X264","ExtraTorrenRG",
                          "Srkfan","UNiQUE","Dvd","DvD","crazy torrent","Spidy","PRiSTiNE","HD","Ganool","TS","BiTo","ARiGOLD","rip","Rets","teh","ChivveZ","song4",
                          "playXD","LIMITED","600MB","700MB","900MB");
                          */
                      foreach ($replace as &$value1){
                      if (strpos($file, $value1) == true) {
                      foreach ($replace as &$value) {
                          $file = str_replace($value, '', $file);
                      }
                      $file = str_replace(' ', '+', $file);
        //             echo $file."<br>";
                // Include the library
                include_once('simple_html_dom.php');
        // assigning the link to $html variable
        //echo "File name ".$file;
        $url='http://www.google.co.in/search?q='.$file.'+imdb';
        //echo "URL ".$url;
        $html = file_get_html($url);
        $flag=0;
        $h="";
        //scraping the link from first result of search
        foreach($html->find('h3[class=r]') as $a){
        foreach($a->find('a') as $e){
        if (strpos($e->href, 'www.imdb.com/title/tt') == true){
        $flag=1;
        $h=$e->href;
        break;
        }
        }
        if($flag==1)
        break;
        }

        if ($h!=NULL) {
          //cleaning the url
          $string=explode("=", $e->href);
          $string=$string[1]; // piece1
          $string=explode("/&", $string);
          $string=$string[0]; // piece1
          $string=explode("/", $string);
          $len = count($string);
          $id = $string[$len-1];
          // assigning the url to $html variable
          $url='http://www.omdbapi.com/?i='.$id.'&plot=short&r=json%27';
          //echo "URL ".$url;
          $details = file_get_html($url);
          $details=explode(',"', $details);
          $limit = count($details);
          ?><tr><?php
          for ($i=0; $i < $limit ; $i++) {
            $details1 = $details[$i];
            if (strpos($details1, 'imdbVotes') !== false) {
              $details1 = str_replace('imdbVotes":"', '', $details1);
              $ratingoutof = str_replace('"', '', $details1);
            }

            if (strpos($details1, 'imdbRating') !== false) {
            $details1 = str_replace('imdbRating":"', '', $details1);
            $rating = str_replace('"', '', $details1);
          }


          if (strpos($details1, 'Title') !== false) {
          $details1 = str_replace('{"Title":"', '', $details1);
          $name = str_replace('"', '', $details1);

        }
          if (strpos($details1, 'Genre') !== false) {
          $details1 = str_replace('Genre":', '', $details1);
          $genre = str_replace('"', '', $details1);
        }

        if (strpos($details1, 'Director') !== false) {
        $details1 = str_replace('Director":', '', $details1);
        $director = str_replace('"', '', $details1);
      }

      if (strpos($details1, 'Writer') !== false) {
      $details1 = str_replace('Writer":', '', $details1);
      $writer = str_replace('"', '', $details1);
    }

    if (strpos($details1, 'Actors') !== false) {
    $details1 = str_replace('Actors":', '', $details1);
    $cast = str_replace('"', '', $details1);
    }
    if (strpos($details1, 'Plot') !== false) {
    $details1 = str_replace('Plot":', '', $details1);
    $plot = str_replace('"', '', $details1);
    }
    if (strpos($details1, 'Released') !== false) {
    $details1 = str_replace('Released":', '', $details1);
    $released = str_replace('"', '', $details1);
    }

        }

        ?>
        <td><?php echo $rating."/10 out of ".$ratingoutof." votes"; ?></td>
        <td><?php echo $name; ?></td>
        <td><?php echo $genre; ?></td>
        <td><?php echo $director; ?></td>
        <td><?php echo $writer; ?></td>
        <td><?php echo $cast; ?></td>
        <td><?php echo $plot; ?></td>
        <td><?php echo $released; ?></td>
      </tr><?php
                  $html->clear();
                  unset($html);
        }
        }
        }
        }
        }
        }
        }
        }
        }
        else{
          ob_end_clean();
          echo "<h2 style'=color:white'>Directory path '". $dir. "' has some issues</h2>";
        }
        }

        listFolderFiles($sdir);
        ?></table></center>

        <center>
        <table>
        <tr><td><a href="getmoviedetails4.php"><button>Back</button></a></td></tr>
        </table>
      </center>
</div>
        </body>
        </html>
      <?php
 }
else
{
?>
<br><br>
<div class="row">
<div class="col-sm-4">
</div>
  <div class="col-sm-4">
  <center>
  <h1 style="color:white">We are Sorry!</h1>
  </center>
  </div>

<div class="col-sm-4">
</div>
</div>

<div class="row">
<div class="col-sm-4">
</div>
  <div class="col-sm-4">
  <center>
  <h1 style="color:white">But you must have an active internet connection to enjoy this functionality.</h1>
  <a href="getmoviedetails4.php"><button>Reload</button></a>
  </center>
  </div>

<div class="col-sm-4">
</div>
</div>
<?php
}

?>
