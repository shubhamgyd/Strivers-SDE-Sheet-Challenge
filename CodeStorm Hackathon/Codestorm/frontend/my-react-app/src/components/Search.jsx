import React from "react";
// import "../../src/Apply.css"

const Search = ({ setSearchKeyword }) => {
  return (
    <div className="header-container">
      <ul>
        <input type="text" placeholder=" Search Here" onChange={(e) => setSearchKeyword(e.target.value)} />
        <i className="fa-solid fa-magnifying-glass"></i>
      </ul>
    </div>
  );
};

export default Search;
