function Select(){
    console.log("Search");
    var type = document.getElementById("type").value;
    var category = document.getElementById("category");
    var subcategory = document.getElementById("subcategory");
    var options1;
    var options2;
    console.log(type);
    console.log(category);
    console.log(subcategory);

    if(type == 1){
        options1 = `<option value="" disabled selected>Choose your option</option>
                    <option value="1">NCC</option>
                    <option value="2">NSS</option>`

        options2 = `<option value="" disabled selected>Choose your option</option>
                    <option value="1">C certificate(os performance)</option>
                    <option value="2">Best NSS Volunteer Awardee(University Level)</option>
                    <option value="3">Participation in National Integration Camp</option>
                    <option value="4">Participation in Pre-Republic Day Parade Camp</option>
                    <option value="5">Best NSS Awardee(State Level/National Level)</option>
                    <option value="6">Participation in Republic Day Parade Camp</option>
                    <option value="7">International Youth Exchange Programme</option>
                    <option value="8">Others</option>`
    }
    else if(type == 2){
        options1 = `<option value="" disabled selected>Choose your option</option>
                    <option value="1">Sports</option>
                    <option value="2">Games</option>`

        options2 = `<option value="" disabled selected>Choose your option</option>
                    <option value="1">College Events</option>
                    <option value="2">Zonal Events</option>
                    <option value="3">State/ University Events</option>
                    <option value="4">National Events</option>
                    <option value="5">International Events</option>`
    }
    else if(type == 3){
        options1 = `<option value="" disabled selected>Choose your option</option>
                    <option value="1">Music</option>
                    <option value="2">Performing Arts</option>
                    <option value="3">Literary Arts</option>`

        options2 = `<option value="" disabled selected>Choose your option</option>
                    <option value="1">College Events</option>
                    <option value="2">Zonal Events</option>
                    <option value="3">State/ University Events</option>
                    <option value="4">National Events</option>
                    <option value="5">International Events</option>`
    }
    else if(type == 4){
        options1 = `<option value="" disabled selected>Choose your option</option>
                    <option value="1">Student Professional Societies (IEEE,IET, ASME, SAE,NASA etc.)</option>
                    <option value="2">College Association Chapters (Mechanical, Civil,Electrical etc.)</option>
                    <option value="3">Festival & Technical Events(College approved)</option>
                    <option value="4">Hobby Clubs</option>
                    <option value="5">Special Initiatives(Approval from College and University is mandatory)</option>`

        options2 = `<option value="" disabled selected>Choose your option</option>
                    <option value="1">Core coordinator</option>
                    <option value="2">Sub coordinator</option>
                    <option value="3">Volunteer</option>`
    }
    else if(type == 5){
        options1 = `<option value="" disabled selected>Choose your option</option>
                    <option value="1">Tech Fest, Tech Quiz</option>
                    <option value="2">MOOC with final assessment certificate</option>
                    <option value="3">Competitions conducted by Professional Societies - (IEEE, IET, ASME, SAE, NASA etc.)</option>
                    <option value="4">Attending Full time Conference/Seminars/Exhibitions/Workshop/STTP conducted at IITs/NITs</option>
                    <option value="5">Paper presentation/publication at IITs/NITs</option>
                    <option value="6">Poster Presentation at IITs/NITs</option>
                    <option value="7">Industrial Training/Internship (at least for 5 full days)</option>
                    <option value="8">Industrial/Exhibition visits</option>
                    <option value="9">Foreign Language Skill (TOFEL/IELTS/BEC exams etc.)</option>`

        options2 = `<option value="" disabled selected>Choose your option</option>
                    <option value="1">College Events</option>
                    <option value="2">Zonal Events</option>
                    <option value="3">State/ University Events</option>
                    <option value="4">National Events</option>
                    <option value="8">International Events</option>`
    }
    else if(type == 6){
        options1 = `<option value="" disabled selected>Choose your option</option>
                    <option value="1">Start-up Company – Registered legally</option>
                    <option value="2">Patent-Filed</option>
                    <option value="3">Patent-Published</option>
                    <option value="4">Patent-Approved</option>
                    <option value="5">Patent-Licensed</option>
                    <option value="6">Prototype developed and tested</option>
                    <option value="7">Awards for Products developed</option>
                    <option value="8">Innovative technologies developed and used by industries/users</option>
                    <option value="9">Got venture capital funding for innovative ideas/products</option>
                    <option value="10">Startup Employment (Offering jobs to two persons less than Rs. 15000/- per month)</option>
                    <option value="11">Societal innovations</option>`

        options2 = `<option value="" disabled selected>No Subcategories for this type</option>`
    }

    category.innerHTML = options1;
    subcategory.innerHTML = options2;
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems);
}

//function Search(){
//    var type = document.getElementById("type").value;
//    var category = document.getElementById("category").value;
//    var subcategory = document.getElementById("subcategory").value;
//    var min = document.getElementById("min").value;
//    var max = document.getElementById("max").value;
//
//    console.log(type, category, subcategory, min, max)
//    if(type != ''){
//        var url = '/staff/search-results/'
//
//        fetch(url, {
//            method:'POST',
//            headers:{
//                'Content-Type':'application/json',
//                'X-CSRFToken':csrftoken,
//            },
//            body:JSON.stringify({'type': type, 'category': category, 'subcategory': subcategory,
//                                 'min': min, 'max': max})
//        })
//        .then((response) =>{
//            return response.json();
//        })
//        .then((data) =>{
//            users = data.users;
//            contentStr = ""
//            users.forEach(function(user){
//                contentStr += `<div class="card-panel teal lighten-2" style="padding: 20px; vertical-align: middle;">
//                                   <a href="/staff/student-details/${user.user_id}"
//                                      style="display:inline;">${user.FirstName} ${user.LastName}</a>
//                               </div>`
//            })
//            document.getElementById('results').innerHTML = contentStr;
//        })
//    }
//}
