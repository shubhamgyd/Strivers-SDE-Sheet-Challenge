import React from "react";
import "../Application.css"

export default function Application(){
    return ( 
        <>
        
        <h1 className="title">Personal Details</h1>
        <div className="container">

        <div className="userdetails">

        <div className="inputfield">
        <label>Applicant First Name</label>
        <input type="text" placeholder="Enter your first name" required/>
        </div>


        <div className="inputfield">
        <label>Applicant Middle Name </label>
        <input type="text" placeholder="Enter your name" required/>
        </div>

        <div className="inputfield">
        <label>Applicant Surname</label>
        <input type="text" placeholder="Enter your name" required/>
        </div>

        <div className="inputfield">
        <label>Applicant Father's Name *</label>
        <input type="text" placeholder="Enter your name" required/>
        </div>

        <div className="inputfield">
        <label>Applicant Mother's Name *</label>
        <input type="text" placeholder="Enter your name" required/>
        </div>

        <div className="inputfield">
        <label>Date of Birth </label>
        <input type="date" placeholder="Enter your name" required/>
        </div>

        <div className="inputfield">
        <label>Gender *</label>
        <input type="text" placeholder="Please select gender" required/>
        </div>

        <div className="inputfield">
        <label>Mobile Number</label>
        <input type="text" placeholder="+91" required/>
        </div>

        <div className="inputfield">
        <label>E-mail Id</label>
        <input type="text" placeholder="Enter your name" required/>
        </div>

        <div className="inputfield">
        <label>Mark of Identification</label>
        <input type="text" required/>
        </div>

        <div className="inputfield">
        <label>Category</label>
        <input type="text" placeholder="Please select category" required/>
        </div>

        <div className="inputfield">
        <label>Blood Group</label>
        <input type="text" placeholder="Please Select Blood Group" required/>
        </div>

        <div className="inputfield">
        <label>Marital Status</label>
        <input type="text" placeholder="Please Select Marital Status" required/>
        </div>

        <div className="inputfield">
        <label>Relation with PwD(Person with Disability) *</label>
        <input type="text" placeholder="Please Select Relation with PwD" required/>
        </div>

        <div className="inputfield">
        <label>Name of Guardian / Caretaker / Attendant / Related person *</label>
        <input type="text" placeholder="" required/>
        </div>

        <div className="inputfield">
        <label>Contact No. of Guardian / Caretaker / Attendant / Related person</label>
        <input type="text" placeholder="+91" required/>
        </div>

        <div className="inputfield">
        <label>Photo *</label>
        <input type="file"  required/>
        </div>

        <div className="inputfield">
        <label>Signature / Thumb / Other Print*</label>
        <input type="file" placeholder="Please Select Relation with PwD" required/>
        </div>

        <div className="inputfield">
        <label>UDID (Unique Disablity ID)*</label>
        <input type="text" placeholder="Enter your UDID" required/>
        </div>

        <div className="inputfield">
        <label>* Marked are compulsory</label>
        <input type="Submit" placeholder="Enter your UDID" required/>
        </div>

        
        </div>

        </div>




        
    </>
    )
}

