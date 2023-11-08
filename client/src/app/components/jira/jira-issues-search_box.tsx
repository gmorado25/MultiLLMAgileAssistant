import React, { FC } from "react";
import { Input } from "@mui/joy";
import SearchIcon from "@mui/icons-material/Search";
import { searchIssues } from "../../utils/jira/api";

const JiraSearchBar: FC = () => {

    const onInitiateSearch = (event: any) => {
        event.preventDefault();
        const query = event.target[0].value;

        console.log("Searching Jira issues with query: " + query);

        searchIssues(
            "https://multi-llm.atlassian.net",
            "rme190001@utdallas.edu",
            query,
        );
    };

    return (
        <div>
            <form onSubmit={onInitiateSearch}>
            <Input 
                startDecorator={<SearchIcon />} 
                placeholder="Search" 
            />
            </form>
        </div>
    );
};

export default JiraSearchBar;