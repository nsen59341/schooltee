function goToLessons(sid) {
    $(".percentage").remove();
    // Get lessons details
    fetch("http://127.0.0.1:8000/teeapp/lessons?studId="+String(sid))
    .then(response => {
        if(!response.ok){
            throw new Error("Network was not Ok! "+response);
        }
        return response.json();
    })
    .then(data => {
        // console.log(data);
        $(".table-container h2").text("Lesson Assigned");

        let html = '';
        data.forEach(el => {
            html += `<tr>
                    <td>${el.title}</td>
                    <td>${el.topic}</td>
                    <td>${el.teacher_details.name}</td>
                    <td><a href="${el.link}" target="_blank">Go</a></td>
                </tr>`;
        });
        $(".table-container tbody").html(html);
    });
}

function goToAssignments(sid) {
    // Get assignments details
    fetch("http://127.0.0.1:8000/teeapp/assignments?studId="+String(sid))
    .then(response => {
        if(!response.ok){
            throw new Error("Network was not Ok!");
        }
        return response.json();
    })
    .then(data => {
        // console.log(data);
        $(".table-container h2").text("Assignment Assigned");
        $(".percentage").remove();
        $(".table-container thead tr").append("<th class='percentage'>Percentage</th>");

        const promiseData = data.map(el => {
            return fetch("http://127.0.0.1:8000/teeapp/performances?assignment_id="+el.id+"&student_id="+sid)
            .then(response => {
                if(!response.ok){
                    throw new Error("Network was not Ok! "+response);
                }
                return response.json();
            })
            .then(data2 => {
                return {
                    'assignment': el,
                    'performance': data2
                }
            });
        });
        return Promise.all(promiseData);
    })

    .then(results => {
        let html = '';
        results.forEach(({ assignment, performance }) => {
            console.log('performance',performance);
            html += `<tr>
                <td>${assignment.lesson_details.title}</td>
                <td>${assignment.lesson_details.topic}</td>
                <td>${assignment.teacher_details.name}</td>
                <td><a href="/assignment/${assignment.id}" target="_blank">Go</a></td>`;
                if(performance.percentage) {
                    html += `<td> ${performance.percentage} </td>`;
                }
                else{   
                    html += `<td> NG </td>`;
                }
                html += `</tr>`;
        });
        $(".table-container tbody").html(html);
    })
    .catch(error => {
        console.error("Error:", error);
    });
}