function safeJSONParse(str){
    try{
        const data = JSON.parse(str);
        return data
    }
    catch(err){
        return "Invalid JSON";
    }
}

const parsed_string = safeJSONParse('{"Name":"Naveen"}')
console.log(parsed_string);

const invalid_parsed_string = safeJSONParse('{"Name":Naveen"}')
console.log(invalid_parsed_string);
