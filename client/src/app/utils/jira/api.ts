import axios from "axios";
import { getCSRFHeader } from "../../utils/cookies"

const TOKEN = "ATATT3xFfGF0i9GV4lt-5sc5ew5jQm-KFYBtSPCHVtbwgulYm_uSvsntKN1tVnGqZrvcqfKFLnUXtMuS9yaBMR4cP_24hArPBacCAr_IU6JN2mn0I-15Lf7qL1OXid-HJoRP83S7NnvthF8OZLUpH9qai0zygvckXyQgyqZOiuAuMQ9Tg7eY9Xk=862FC402"

/*
 * Cosntructs the header information for the Jira API
 * call authentication via Http Basic Auth.
 */
const constructAPIHeaders = (email: string) => {
    const token = TOKEN;
    const auth = email + ":" + token;

    const headers = {
        "Authorization": `Basic ${Buffer.from(auth).toString("base64")}`,
        "Accept": "application/json"
    }
    return headers;
}

/*
 * Cosntructs the full issue search URL to pass to Jira
 * based on the given site, and query parameters.
 */
const constructSearchURL = (
    domain: string, 
    query?: string, 
    projectID?: string
) => {
    let url = new URL(domain + "/rest/api/3/issue/picker");
    if (query)
        url.searchParams.append("query", query);
    if (projectID)
        url.searchParams.append("projectID", projectID);
    return url
};

const constructIssueURL = (
    domain: string,
    issueID: string,
    fields?: string[]
) => {
    let url = new URL(domain + "/rest/api/3/issue/" + issueID);
    if (fields)
        fields.forEach((field) => url.searchParams.append("fields", field))
    return url
}

export const searchIssues = async (
    domain: string, 
    email: string,
    query?: string, 
    projectID?: string
) => {
    try {
        const cloud_url = constructSearchURL(domain, query, projectID);
        const body = JSON.stringify({
            "url": cloud_url.toString(),
            "header": constructAPIHeaders(email)
        });

        axios.post("/jira/", body, getCSRFHeader()).then((response: any) => {
            const data = response.data;
            console.log(response)
            // set the search results in UI here for issue list
        });
    } catch (err) {
        console.log(err);
    }
    return;
};

export const getIssueInfo = async (
    domain: string, 
    email: string,
    issueID: string,
    fields?: string[]
) => {
    try {
        const cloud_url = constructIssueURL(domain, issueID, fields);
        const body = JSON.stringify({
            "url": cloud_url.toString(),
            "header": constructAPIHeaders(email)
        });
        axios.post("/jira/", body, getCSRFHeader()).then((response: any) => {
            const data = response.data;
            console.log(response)
            // set the search result in UI here for full issue report (summary, description, etc.)
        });
    } catch (err) {
        console.log(err);
    }
};