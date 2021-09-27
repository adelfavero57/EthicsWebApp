



$('document').ready(function(){

    $('#search').keyup(function(e){
      
      let value = $(this).val().toLowerCase();

      $(".tbody").filter(function() {

        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
      
    });
});


function sortTitle(){
    const rows = Array.from(document.querySelectorAll(".tbody"));
   
    const sortedRows = rows.sort((a, b) => {

        const aText = a.querySelectorAll("td")[1];
        const bText = b.querySelectorAll("td")[1];

        if(aText.textContent > bText.textContent){
            return -1;
        }

        if(aText.textContent.toLowerCase() < bText.textContent.toLowerCase()){
            return 1;
        }

        return 0;
    })


    let newRows = document.getElementsByClassName("tbody");


    newRows = [...sortedRows];



  };




