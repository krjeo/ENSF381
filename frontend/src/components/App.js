import React, { Component } from "react";
import { render } from "react-dom";
import HomePage from "./HomePage";
import BrowseBooks from "./BrowseBooks";
import SingleBook from "./SingleBook";

export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() { // If you want to center a page use <div className="center">
    return (
    <div> 
      <BrowseBooks />
      </div>
    );
  }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);
