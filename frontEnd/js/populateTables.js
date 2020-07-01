
$(document).ready(function() {
    var API_URL = "https://o3uuqjbs00.execute-api.us-east-2.amazonaws.com/prod/getdata"
    var returnedObject = {}
        $.ajax({
            type: 'GET',
            url: API_URL,

            success: function(data) {
                returnedObject = data
                const table = document.getElementsByClassName('table100-body')
                let count = 0;
                returnedObject.body['Items'].forEach(function(item) {

                    var row = document.createElement("tr");

                    var column1 = document.createElement("td");
                    column1.className ="cell100 column1";
                    column1.id = "title" + count;
                    row.appendChild(column1);

                    var column2 = document.createElement("td");
                    column2.className ="cell100 column2";
                    column2.id = "location"+ count;
                    row.appendChild(column2);

                    var column3 = document.createElement("td");
                    column3.className ="cell100 column3";
                    column3.id = "company" + count;
                    row.appendChild(column3);

                    var column4 = document.createElement("td");
                    column4.className ="cell100 column4";
                    column4.id = "website"+ count;
                    row.appendChild(column4);

                    var column5 = document.createElement("td");
                    column5.className ="cell100 column5";
                    column5.id = "salary"+ count;
                    row.appendChild(column5);
                    
                    table[0].children[0].appendChild(row)
                    count = count+1

                    if (item.WEBSITE === "simplyhired.com") {
                        document.getElementById(column1.id).innerText = item.TITLE;
                        document.getElementById(column2.id).innerText = item.LOCATION;
                        document.getElementById(column3.id).innerText = item.COMPANY;
                        document.getElementById(column4.id).innerText = item.WEBSITE;
                    } else {
                        document.getElementById(column1.id).innerText = item.TITLE;
                        document.getElementById(column2.id).innerText = item.LOCATION;
                        document.getElementById(column3.id).innerText = item.COMPANY;
                        document.getElementById(column4.id).innerText = item.WEBSITE;
                        document.getElementById(column5.id).innerText = item.SALARY;
                    }
                })
            }
        })
})
