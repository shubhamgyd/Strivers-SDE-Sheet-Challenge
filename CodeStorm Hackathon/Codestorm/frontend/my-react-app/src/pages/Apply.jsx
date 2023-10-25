import data from "../data.json";
import Jobs from "../components/Jobs";
import { useState } from "react";
import Header2 from "../components/Header2";
import Search from "../components/Search";
import "../../src/Apply.css"
// import "../images/"

function Apply() {
  const [filterKeywords, setfilterKeywords] = useState([]);

  const setSearchKeyword = (data) => {
    setfilterKeywords(data);
  };

  const addFilterKeywords = (data) => {
    if (!filterKeywords.includes(data)) {
      setfilterKeywords([...filterKeywords, data]);
    }
  };

  const deleteKeyword = (data) => {
    const newKeywords = filterKeywords.filter((key) => key !== data);
    setfilterKeywords(newKeywords);
  };

  const clearAll = () => {
    setfilterKeywords([]);
  };

  return (
    <div>
      {/* <div className="header"></div> */}

      <Search setSearchKeyword={setSearchKeyword}  />
      

      {/* {filterKeywords.length > 0 && (
        <Header2
          keywords={filterKeywords}
          removeKeywords={deleteKeyword}
          clearAll={clearAll}
        />
      )} */}

      <Jobs
        keywords={filterKeywords}
        data={data}
        setKeywords={addFilterKeywords}
      />
    </div>
  );
}

export default Apply;
