console.log("file connected ")


const wrapper = document.getElementById('wrapper');

fetch('http://localhost:5000/aligment')
.then(function(response) {
  return response.json();
})
.then(function(data) {
    console.log(data)

    let arr_str = data.data
let temp =arr_str.replace(/'/g, '"');
var array = JSON.parse(temp);
  






let template = ``
var index=0;
array.forEach(element => {
    index++;
    idForm="form"+index;
    idTextarea="textProposition"+index;
    idSentence="sentence"+index;
    idRadioanswer="radAnswer"+index;
    template = `${template} 
    
    
     <form class="py-6" id="${idForm}" >
            <div dir="rtl" class="flex bg-blue-100 m-5 rounded-lg p-3  ">
                <p  lang="ar" class="ml-3 text-sm text-blue-700" >${index}</p>
                <p  lang="ar" class="ml-3 text-sm text-blue-700" id="${idSentence}">${element[0]}</p>
            </div>
            <div class="mx-10 my-6">
                <div class="flex bg-red-100 form-check m-5 rounded-lg p-3">
                    <input type="radio" class=" w-5 h-5 text-red-700 cursor-pointer" name="${idRadioanswer}" value="${element[1][0]}">
                    <p class="ml-3 text-sm text-red-700">${element[1][0]}</p>
                </div>
                <div class="flex form-check bg-red-100 m-5 rounded-lg p-3">
                    <input type="radio" class="w-5 h-5 text-red-700 cursor-pointer" name="${idRadioanswer}" value="${element[1][1]}">
                
                    <p class="ml-3 text-sm text-red-700">${element[1][1]}</p>
                </div>
                <div class="flex form-check bg-red-100 m-5 rounded-lg p-3" id="hih">
                    <input type="radio" class="w-5 h-5 text-red-700 cursor-pointer" name="${idRadioanswer}" value="${element[1][2]}" >
                
                    <p class="ml-3 text-sm text-red-700">${element[1][2]}</p>
                </div>
            </div>

            <div class=" m-5 rounded-lg px-3 pb-1">
                <p class="ml-3 text-sm text-blue-700">
                    <span class="font-medium">Veuillez ecrire votre proposition : </span>
                </p>
                <textarea id="${idTextarea}"
                    class="h-16 w-full  p-1 text-base text-gray-700 placeholder-gray-600 border rounded-lg focus:shadow-outline"></textarea>
            </div>

<div class="flex items-center justify-center">
            <button type= "button" onclick = "required('${idSentence}','${idTextarea}','${idRadioanswer}')"  
            class= "p-2 px-6 text-sm font-medium rouned-lg border border-blue-600 text-blue-600 hover:bg-blue-600 hover:text-white ">
            Save 
            </button>

            </div>
            

        </form>
    

    
    `
    
});

    wrapper.innerHTML=template


   
});

var rows =[];
rows.push(['Sentence','Translated sentence'])

//method to download all datas as a .csv file
function exportData(){
    console.log(rows)
    csvContent = "data:text/csv;charset=UTF-8,%EF%BB%BF";
    rows.forEach(function(rowArray){
        row = rowArray.join(",");
        csvContent += row + "\r\n";
    });
    /* create a hidden <a> DOM node and set its download attribute */
    var link = document.createElement("a");
    link.setAttribute("href", csvContent);
    link.setAttribute("download", "Data.csv");
    document.body.appendChild(link);
    link.click();
}


//Function to save In sheets
function required(idSentence,idTextarea,nameRadAnswer)
{
    var sentence=document.getElementById(idSentence).textContent;
    var empt = document.getElementById(idTextarea);
    if (empt.value.length == 0)
    {
        var query='input[name='+nameRadAnswer+']:checked'
         var checkRadio = document.querySelector(query);
            if(checkRadio != null) {
                rows.push([sentence,checkRadio.value])
                console.log(sentence)
                console.log(checkRadio.value)
            }
            else {
                alert("Please chooose one of the above suggestions :")
            }
        return false;
    }
    else
    {
        rows.push([sentence,empt.value])
        console.log(sentence)
        console.log(empt.value)
        return true;
    }
}