import React from "react";
import "../diff.css"

export default function Difficulties(){
    return ( 
        <>
        
        <h1 className="title">Functional Difficulties faced</h1>

        <form id="form-diff">

        <h1 title>Vision</h1>

        <div className="form_control">
            <label className="question">
            1.[Do/Does] [you/he/she] wear glasses?
            </label> 
            <label htmlFor="Male"><input type="radio" name="1"/>Yes</label>
            <label htmlFor="Male"><input type="radio" name="1"/>No</label>
            <label htmlFor="Male"><input type="radio" name="1"/>Refused</label>
            <label htmlFor="Male"><input type="radio" name="1"/>Don't know</label>
        </div>

        <div className="form_control">
            <label className="question">
            2.[Do/Does] [you/he/she] have difficulty seeing, even when wearing
[your/his/her] glasses? Would you say…  
            </label> 
            <label htmlFor="Male"><input type="radio" name="2"/>No difficulty </label>
            <label htmlFor="Male"><input type="radio" name="2"/>Some difficulty</label>
            <label htmlFor="Male"><input type="radio" name="2"/>A lot of difficulty</label>
            <label htmlFor="Male"><input type="radio" name="2"/>Cannot do at all</label>
            <label htmlFor="Male"><input type="radio" name="2"/>Refused</label>
            <label htmlFor="Male"><input type="radio" name="2"/>Don't know</label>
        </div>

        <div className="form_control">
            <label className="question">
            3.[Do/does] [you/he/she] have difficulty clearly seeing the picture on a coin
even when wearing [your/his/her] glasses? Would you say… [Read response
categories]? 
            </label> 
            <label htmlFor="Male"><input type="radio" name="3"/>No difficulty </label>
            <label htmlFor="Male"><input type="radio" name="3"/>Some difficulty</label>
            <label htmlFor="Male"><input type="radio" name="3"/>A lot of difficulty</label>
            <label htmlFor="Male"><input type="radio" name="3"/>Cannot do at all</label>
            <label htmlFor="Male"><input type="radio" name="3"/>Refused</label>
            <label htmlFor="Male"><input type="radio" name="3"/>Don't know</label>
        </div>

        <h1 title>Hearing</h1>

        <div className="form_control">
            <label className="question">
            4.[Do/Does] [you/he/she] use a hearing aid?
            </label> 
            <label htmlFor="Male"><input type="radio" name="4"/>Yes</label>
            <label htmlFor="Male"><input type="radio" name="4"/>No</label>
            <label htmlFor="Male"><input type="radio" name="4"/>Refused</label>
            <label htmlFor="Male"><input type="radio" name="4"/>Don't know</label>
        </div>

        <div className="form_control">
            <label className="question">
            5.[Do/Does] [you/he/she] have difficulty hearing,  even when using a
hearing aid(s)? Would you say… 
            </label> 
            <label htmlFor="Male"><input type="radio" name="5"/>No difficulty </label>
            <label htmlFor="Male"><input type="radio" name="5"/>Some difficulty</label>
            <label htmlFor="Male"><input type="radio" name="5"/>A lot of difficulty</label>
            <label htmlFor="Male"><input type="radio" name="5"/>Cannot do at all</label>
            <label htmlFor="Male"><input type="radio" name="5"/>Refused</label>
            <label htmlFor="Male"><input type="radio" name="5"/>Don't know</label>
        </div>

        <div className="form_control">
            <label className="question">
            6.[Do/does] [you/he/she] have difficulty hearing what is said in a conversation with one
other person in a quiet room even when using [your/his/her] hearing
aid(s)? Would you say… 
            </label> 
            <label htmlFor="Male"><input type="radio" name="6"/>No difficulty </label>
            <label htmlFor="Male"><input type="radio" name="6"/>Some difficulty</label>
            <label htmlFor="Male"><input type="radio" name="6"/>A lot of difficulty</label>
            <label htmlFor="Male"><input type="radio" name="6"/>Cannot do at all</label>
            <label htmlFor="Male"><input type="radio" name="6"/>Refused</label>
            <label htmlFor="Male"><input type="radio" name="6"/>Don't know</label>
        </div>

        <div className="form_control">
            <label className="question">
            7.[Do/does] [you/he/she] have difficulty hearing what is said in a conversation with one
other person in a noisier room even when using [your/his/her] hearing
aid(s)? Would you say… 
            </label> 
            <label htmlFor="Male"><input type="radio" name="7"/>No difficulty </label>
            <label htmlFor="Male"><input type="radio" name="7"/>Some difficulty</label>
            <label htmlFor="Male"><input type="radio" name="7"/>A lot of difficulty</label>
            <label htmlFor="Male"><input type="radio" name="7"/>Cannot do at all</label>
            <label htmlFor="Male"><input type="radio" name="7"/>Refused</label>
            <label htmlFor="Male"><input type="radio" name="7"/>Don't know</label>
        </div>

        <h1 title>Mobility</h1>

        <div className="form_control">
            <label className="question">
            8.[Do/Does] [you/he/she] have difficulty walking or climbing steps? Would you say…
            </label> 
            <label htmlFor="Male"><input type="radio" name="8"/>No difficulty </label>
            <label htmlFor="Male"><input type="radio" name="8"/>Some difficulty</label>
            <label htmlFor="Male"><input type="radio" name="8"/>A lot of difficulty</label>
            <label htmlFor="Male"><input type="radio" name="8"/>Cannot do at all</label>
            <label htmlFor="Male"><input type="radio" name="8"/>Refused</label>
            <label htmlFor="Male"><input type="radio" name="8"/>Don't know</label>
        </div>

        <div className="form_control">
            <label className="question">
            9.[Do/does] [you/he/she] use any equipment or receive help for getting around?
            </label> 
            <label htmlFor="Male"><input type="radio" name="9"/>Yes</label>
            <label htmlFor="Male"><input type="radio" name="9"/>No</label>
            <label htmlFor="Male"><input type="radio" name="9"/>Refused</label>
            <label htmlFor="Male"><input type="radio" name="9"/>Don't know</label>
        </div>

        <div className="form_control">
            <label className="question">
            10.[Do/Does] [you/he/she] have difficulty walking 100 meters on level ground, that would
be about the length of one football field or one city block without the use
of [your/his/her] aid? Would you say… 
            </label> 
            <label htmlFor="Male"><input type="radio" name="10"/>No difficulty </label>
            <label htmlFor="Male"><input type="radio" name="10"/>Some difficulty</label>
            <label htmlFor="Male"><input type="radio" name="10"/>A lot of difficulty</label>
            <label htmlFor="Male"><input type="radio" name="10"/>Cannot do at all</label>
            <label htmlFor="Male"><input type="radio" name="10"/>Refused</label>
            <label htmlFor="Male"><input type="radio" name="10"/>Don't know</label>
        </div>


        <div className="form_control">
            <label className="question">
            11.[Do/does] [you/he/she] use any of the following?
            </label> 
            <label htmlFor="Male"><input type="checkbox" name="10"/>Cane or walking stick? </label>
            <label htmlFor="Male"><input type="checkbox" name="10"/>Walker or Zimmer frame?</label>
            <label htmlFor="Male"><input type="checkbox"name="10"/>Crutches?</label>
            <label htmlFor="Male"><input type="checkbox"name="10"/>Wheelchair or scooter?</label>
            <label htmlFor="Male"><input type="checkbox" name="10"/>Artificial limb (leg/foot)?</label>
            <label htmlFor="Male"><input type="checkbox" name="10"/>Someone’s assistance?</label>
            <label htmlFor="Male"><input type="checkbox" name="10"/>Other(please specify):</label>
            <input type="text" />
        </div>



        <div className="form_control">
            <label className="question">
            12.[Do/Does] [you/he/she] have difficulty walking half a km on level ground, that would be
the length of five football fields or five city blocks without the use of
[your/his/her] aid? Would you say… 
            </label> 
            <label htmlFor="Male"><input type="radio" name="2"/>No difficulty </label>
            <label htmlFor="Male"><input type="radio" name="2"/>Some difficulty</label>
            <label htmlFor="Male"><input type="radio" name="2"/>A lot of difficulty</label>
            <label htmlFor="Male"><input type="radio" name="2"/>Cannot do at all</label>
            <label htmlFor="Male"><input type="radio" name="2"/>Refused</label>
            <label htmlFor="Male"><input type="radio" name="2"/>Don't know</label>
        </div>

        <div className="form_control">
            <label className="question">
            13.[Do/Does] [you/he/she] have difficulty walking up or down 12 steps? Would you say… 
            </label> 
            <label htmlFor="Male"><input type="radio" name="2"/>No difficulty </label>
            <label htmlFor="Male"><input type="radio" name="2"/>Some difficulty</label>
            <label htmlFor="Male"><input type="radio" name="2"/>A lot of difficulty</label>
            <label htmlFor="Male"><input type="radio" name="2"/>Cannot do at all</label>
            <label htmlFor="Male"><input type="radio" name="2"/>Refused</label>
            <label htmlFor="Male"><input type="radio" name="2"/>Don't know</label>
        </div>

        <div className="form_control">
            <label className="question">
            14.[Do/Does] [you/he/she] have difficulty walking 100 meters on level ground, that would
be about the length of one football field or one city block, when using [your/his/her] aid?
Would you say…  
            </label> 
            <label htmlFor="Male"><input type="radio" name="2"/>No difficulty </label>
            <label htmlFor="Male"><input type="radio" name="2"/>Some difficulty</label>
            <label htmlFor="Male"><input type="radio" name="2"/>A lot of difficulty</label>
            <label htmlFor="Male"><input type="radio" name="2"/>Cannot do at all</label>
            <label htmlFor="Male"><input type="radio" name="2"/>Refused</label>
            <label htmlFor="Male"><input type="radio" name="2"/>Don't know</label>
        </div>

        <div className="form_control">
            <label className="question">
            15.[Do/Does] [you/he/she] have difficulty walking half a km on level ground, that would be
the length of five football fields or five city blocks, when using [your/his/her] aid?
Would you say… 
            </label> 
            <label htmlFor="Male"><input type="radio" name="2"/>No difficulty </label>
            <label htmlFor="Male"><input type="radio" name="2"/>Some difficulty</label>
            <label htmlFor="Male"><input type="radio" name="2"/>A lot of difficulty</label>
            <label htmlFor="Male"><input type="radio" name="2"/>Cannot do at all</label>
            <label htmlFor="Male"><input type="radio" name="2"/>Refused</label>
            <label htmlFor="Male"><input type="radio" name="2"/>Don't know</label>
        </div>

        <h1 title>Communication</h1>

        <div className="form_control">
            <label className="question">
           16.Using [your/his/her] usual language, [do/does] [you/he/she] have difficulty
communicating, for example understanding or being understood? Would you say… 
            </label> 
            <label htmlFor="Male"><input type="radio" name="2"/>No difficulty </label>
            <label htmlFor="Male"><input type="radio" name="2"/>Some difficulty</label>
            <label htmlFor="Male"><input type="radio" name="2"/>A lot of difficulty</label>
            <label htmlFor="Male"><input type="radio" name="2"/>Cannot do at all</label>
            <label htmlFor="Male"><input type="radio" name="2"/>Refused</label>
            <label htmlFor="Male"><input type="radio" name="2"/>Don't know</label>
        </div>

        <div className="form_control">
            <label className="question">
            17.[Do/does] [you/he/she] use sign language?
            </label> 
            <label htmlFor="Male"><input type="radio" name="4"/>Yes</label>
            <label htmlFor="Male"><input type="radio" name="4"/>No</label>
            <label htmlFor="Male"><input type="radio" name="4"/>Refused</label>
            <label htmlFor="Male"><input type="radio" name="4"/>Don't know</label>
        </div>

        <h1 title>Cognition(Remembering)</h1>

        <div className="form_control">
            <label className="question">
            18.[Do/does] [you/he/she] have difficulty remembering or concentrating? Would you say…
            </label> 
            <label htmlFor="Male"><input type="radio" name="2"/>No difficulty </label>
            <label htmlFor="Male"><input type="radio" name="2"/>Some difficulty</label>
            <label htmlFor="Male"><input type="radio" name="2"/>A lot of difficulty</label>
            <label htmlFor="Male"><input type="radio" name="2"/>Cannot do at all</label>
            <label htmlFor="Male"><input type="radio" name="2"/>Refused</label>
            <label htmlFor="Male"><input type="radio" name="2"/>Don't know</label>
        </div>

        <div className="form_control">
            <label className="question">
            19.[Do/does] [you/he/she] have difficulty remembering, concentrating, or both? Would you
say… 
            </label> 
            <label htmlFor="Male"><input type="radio" name="4"/>Difficulty remembering only</label>
            <label htmlFor="Male"><input type="radio" name="4"/>Difficulty concentrating only</label>
            <label htmlFor="Male"><input type="radio" name="4"/>Difficulty with both remembering and concentrating </label>
            <label htmlFor="Male"><input type="radio" name="2"/>Refused</label>
            <label htmlFor="Male"><input type="radio" name="4"/>Don't know</label>
        </div>

        <div className="form_control">
            <label className="question">
            20.How often [do/does] [you/he/she] have difficulty remembering? Would you say… 
            </label> 
            <label htmlFor="Male"><input type="radio" name="4"/>Sometimes</label>
            <label htmlFor="Male"><input type="radio" name="4"/>Often</label>
            <label htmlFor="Male"><input type="radio" name="4"/>All of the time</label>
            <label htmlFor="Male"><input type="radio" name="2"/>Refused</label>
            <label htmlFor="Male"><input type="radio" name="4"/>Don't know</label>
        </div>

<div className="form_control">
            <label className="question">
            21.[Do/does] [you/he/she] have difficulty remembering a few things, a lot of things, or
almost everything? Would you say…
            </label> 
            <label htmlFor="Male"><input type="radio" name="4"/>A few things</label>
            <label htmlFor="Male"><input type="radio" name="4"/>A lot of things</label>
            <label htmlFor="Male"><input type="radio" name="4"/>Almost everything</label>
            <label htmlFor="Male"><input type="radio" name="2"/>Refused</label>
            <label htmlFor="Male"><input type="radio" name="4"/>Don't know</label>
        </div>

        <h1 title>Self Care</h1>

        <div className="form_control">
            <label className="question">
            22.[Do/does] [you/he/she] have difficulty with self care, such as washing all over or
dressing? Would you say… 
            </label> 
            <label htmlFor="Male"><input type="radio" name="2"/>No difficulty </label>
            <label htmlFor="Male"><input type="radio" name="2"/>Some difficulty</label>
            <label htmlFor="Male"><input type="radio" name="2"/>A lot of difficulty</label>
            <label htmlFor="Male"><input type="radio" name="2"/>Cannot do at all</label>
            <label htmlFor="Male"><input type="radio" name="2"/>Refused</label>
            <label htmlFor="Male"><input type="radio" name="2"/>Don't know</label>
        </div>

        <h1 title>Affect (Anxiety and Depression)</h1>

        <div className="form_control">
            <label className="question">
            23.How often [do/does] [you/he/she] feel worried, nervous or anxious? Would you say… 
            </label> 
            <label htmlFor="Male"><input type="radio" name="2"/>No difficulty </label>
            <label htmlFor="Male"><input type="radio" name="2"/>Some difficulty</label>
            <label htmlFor="Male"><input type="radio" name="2"/>A lot of difficulty</label>
            <label htmlFor="Male"><input type="radio" name="2"/>Cannot do at all</label>
            <label htmlFor="Male"><input type="radio" name="2"/>Refused</label>
            <label htmlFor="Male"><input type="radio" name="2"/>Don't know</label>
        </div>

        <div className="form_control">
            <label className="question">
           24.[Do/Does] [you/he/she] take medication for these feelings?
            </label> 
            <label htmlFor="Male"><input type="radio" name="4"/>Yes</label>
            <label htmlFor="Male"><input type="radio" name="4"/>No</label>
            <label htmlFor="Male"><input type="radio" name="4"/>Refused</label>
            <label htmlFor="Male"><input type="radio" name="4"/>Don't know</label>
        </div>

        <div className="form_control">
            <label className="question">
            25.Thinking about the last time [you/he/she] felt worried, nervous or anxious, how would
[you/he/she] describe the level of these feelings? Would [you/he/she] say… 
            </label> 
            <label htmlFor="Male"><input type="radio" name="4"/>A little</label>
            <label htmlFor="Male"><input type="radio" name="4"/>A lot</label>
            <label htmlFor="Male"><input type="radio" name="4"/>Somewhere in between a little and lot</label>
            <label htmlFor="Male"><input type="radio" name="4"/>Refused</label>
            <label htmlFor="Male"><input type="radio" name="4"/>Don't know</label>
        </div>

        <div className="form_control">
            <label className="question">
            26.How often [do/does] [you/he/she] feel depressed? Would [you/he/she] say… 
            </label> 
            <label htmlFor="Male"><input type="radio" name="4"/>Daily</label>
            <label htmlFor="Male"><input type="radio" name="4"/>Weekly</label>
            <label htmlFor="Male"><input type="radio" name="4"/>Monthly</label>
            <label htmlFor="Male"><input type="radio" name="4"/>Refused</label>
            <label htmlFor="Male"><input type="radio" name="4"/>Don't know</label>
        </div>

        <div className="form_control">
            <label className="question">
            27.[Do/Does] [you/he/she] take medication for depression?
            </label> 
            <label htmlFor="Male"><input type="radio" name="4"/>Yes</label>
            <label htmlFor="Male"><input type="radio" name="4"/>No</label>
            <label htmlFor="Male"><input type="radio" name="4"/>Refused</label>
            <label htmlFor="Male"><input type="radio" name="4"/>Don't know</label>
        </div>

        <div className="form_control">
            <label className="question">
            28.Thinking about the last time [you/he/she] felt worried, nervous or anxious, how would
[you/he/she] describe the level of these feelings? Would [you/he/she] say… 
            </label> 
            <label htmlFor="Male"><input type="radio" name="4"/>A little</label>
            <label htmlFor="Male"><input type="radio" name="4"/>A lot</label>
            <label htmlFor="Male"><input type="radio" name="4"/>Somewhere in between a little and lot</label>
            <label htmlFor="Male"><input type="radio" name="4"/>Refused</label>
            <label htmlFor="Male"><input type="radio" name="4"/>Don't know</label>
        </div>


        </form>
    </>
    )
}

