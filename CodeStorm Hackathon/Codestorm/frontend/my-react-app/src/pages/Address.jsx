import React from "react";
import "../Application.css"

export default function Address(){
    return ( 
        <>
        
        <h1 className="title">Address for Correspondence</h1>
        <div className="container">

        <div className="userdetails">

        <div className="inputfield">
        <label>Address Line 1</label>
        <input type="text"  required/>
        </div>

        <div className="inputfield">
        <label>Address Line 2 </label>
        <input type="text"  required/>
        </div>

        <div className="inputfield">
        <label>Address Line 3</label>
        <input type="text"  required/>
        </div>

        <div className="inputfield">
        <label>State / UTs *</label>
        <input type="text" placeholder="Choose State / UTs " required/>
        </div>

        <div className="inputfield">
        <label>District *</label>
        <input type="text" placeholder="Choose District " required/>
        </div>

        <div className="inputfield">
        <label>City / Sub District / Tehsil *</label>
        <input type="text" placeholder="Choose City / Sub District / Tehsil " required/>
        </div>

        <div className="inputfield">
        <label>Village / Block</label>
        <input type="text" placeholder="Choose Village / Block" required/>
        </div>

        <div className="inputfield">
        <label>Pincode *</label>
        <input type="text"  required/>
        </div>

        <div className="inputfield">
        <label>Nature of Document for Address Proof *</label>
        <input type="text" placeholder="Please Select Nature of Document" required/>
        </div>

        <div className="inputfield">
        <label>Upload Proof of Correspondence Address*</label>
        <input type="file" required/>
        </div>

        <div className="inputfield">
        <label>* Marked are compulsory</label>
        <input type="Submit" required/>
        </div>

        
        
        </div>

        </div>
        
    </>
    )
}