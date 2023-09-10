

function updateRecords(records, id, prop, value) {
    if (value == "" ) { 
        delete records.id[prop];
    }
    else if (  records[id][prop] != "tracks" && value != "" ) { 
       records[id][prop] = value;
    }
    else if ( records[id][prop] == "tracks" && value != "") { 
        if (records[id][prop] == false) { 
           records.id[prop] = []; 
            records.id[prop].push(value);
        } else { 
            records.id[prop].push(value)
        }
    }
  return records;

}
