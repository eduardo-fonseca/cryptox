<?php

    ini_set('display_errors', 1);
    include_once("includes/functions.php");

?>

<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <link rel="icon" type="image/png" href="assets/img/favicon.ico">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    
    <title>CryptoX</title>

    <meta content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0" name="viewport" />
    
    <link href="assets/css/bootstrap.css" rel="stylesheet" />
    <link href="assets/css/fresh-bootstrap-table.css" rel="stylesheet" />
    <link href="assets/css/extra.css" rel="stylesheet" />

    <!--     Fonts and icons     -->
    <link href="http://maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css" rel="stylesheet">
    <link href='http://fonts.googleapis.com/css?family=Roboto:400,700,300' rel='stylesheet' type='text/css'>
	
	
</head>
<body>


<div class="wrapper">
    <div class="fresh-table full-color-azure full-screen-table">
    <!--    Available colors for the full background: full-color-blue, full-color-azure, full-color-green, full-color-red, full-color-orange                  
            Available colors only for the toolbar: toolbar-color-blue, toolbar-color-azure, toolbar-color-green, toolbar-color-red, toolbar-color-orange
    -->
        
        <div class="toolbar">
            <button id="alertBtn" class="btn btn-default">CRYPTOX</button>
        </div>
		
        
        <table id="fresh-table" class="table">
            <thead>
                <th data-field="exchange">Exchange</th>
                <th data-field="last_price">Último Preço</th>
                <th data-field="ask">Preço Compra</th>
                <th data-field="bid">Preço Venda</th>
            </thead>
            <tbody id="cpxTbody">
                <tr>
                    <td>BitStamp</td>
                    <td>$ <?php echo cpxBitStamp()[1]; ?></td>
                    <td>$ <?php echo cpxBitStamp()[8]; ?></td>
                    <td>$ <?php echo cpxBitStamp()[4]; ?></td>
                </tr>
                <tr>
                <tr>
                    <td>Gemini</td>
                    <td>$ <?php echo cpxGemini()[3]; ?></td>
                    <td>$ <?php echo cpxGemini()[1]; ?></td>
                    <td>$ <?php echo cpxGemini()[2]; ?></td>
                </tr>
                <tr>
                    <td>Cex.IO</td>
                    <td>$ <?php echo cpxCexIO()[1]; ?></td>
                    <td>$ <?php echo cpxCexIO()[8]; ?></td>
                    <td>$ <?php echo cpxCexIO()[7]; ?></td>
                </tr>
                <tr>
                    <td>HitBTC</td>
                    <td>$ <?php echo cpxHitBTC()[1]; ?></td>
                    <td>$ <?php echo cpxHitBTC()[5]; ?></td>
                    <td>$ <?php echo cpxHitBTC()[6]; ?></td>
                </tr>
                <tr>
                    <td>Poloniex</td>
                    <td>$ <?php echo cpxPoloniex()[1]; ?></td>
                    <td>$ <?php echo cpxPoloniex()[2]; ?></td>
                    <td>$ <?php echo cpxPoloniex()[3]; ?></td>
                </tr>
                <tr>
                    <td>Bitfinex</td>
                    <td>$ <?php echo cpxBitfinex()[1]; ?></td>
                    <td>$ <?php echo cpxBitfinex()[6]; ?></td>
                    <td>$ <?php echo cpxBitfinex()[2]; ?></td>
                </tr>
            </tbody>
        </table>
		
    </div>
    
</div>


</body>
    <script type="text/javascript" src="assets/js/jquery-1.11.2.min.js"></script>
    <script type="text/javascript" src="assets/js/bootstrap.js"></script>
    <script type="text/javascript" src="assets/js/bootstrap-table.js"></script>
        
    <script type="text/javascript">
        var $table = $('#fresh-table'),
            $alertBtn = $('#alertBtn'), 
            full_screen = false,
            window_height;
            
        $().ready(function(){

            $('#cpxTbody').on('change', function () {
                $(this).addClass('blinking');
            });

            window_height = $(window).height();
            table_height = window_height - 20;
            
            
            $table.bootstrapTable({
                toolbar: ".toolbar",

                showRefresh: false,
                search: false,
                showToggle: false,
                showColumns: false,
                pagination: true,
                striped: true,
                sortable: false,
                height: table_height,
                pageSize: 25,
                pageList: [25,50,100],
                
                formatShowingRows: function(pageFrom, pageTo, totalRows){
                    //do nothing here, we don't want to show the text "showing x of y from..." 
                },
                formatRecordsPerPage: function(pageNumber){
                    return pageNumber + " rows visible";
                },
                icons: {
                    refresh: 'fa fa-refresh',
                    toggle: 'fa fa-th-list',
                    columns: 'fa fa-columns',
                    detailOpen: 'fa fa-plus-circle',
                    detailClose: 'fa fa-minus-circle'
                }
            });
            
            
            $alertBtn.click(function () {
                alert("Developed by Eduardo Fonseca.");
            });

            setInterval(function(){ 
               $("#cpxTbody").load(location.href + " #cpxTbody>*", "");
            },1000);

                    
            $(window).resize(function () {
                $table.bootstrapTable('resetView');
            });    
        });
       
    </script>

</html>