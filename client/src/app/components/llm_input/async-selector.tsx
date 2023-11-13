"use client";
import axios from "axios";
import React, { FC, useState, useEffect } from "react";
import { MenuItem, Select } from "@mui/material";
import { getJSONHeader } from "@/app/utils/cookies";

interface SelectorProperties {
    url: string, 
    placeholder: string,
    callback: (arg: any) => void
};

/**
 * Component designed to display a list of dynamic options loaded
 * from the given URL origin.
 * 
 * @param selection Field containing the URL to retrieve available options 
 *                  from and a default value before the user makes a choice.
 * 
 * @returns Returns a drop-down menu component made of the list of selections 
 *          retrieved from the given origin.
 */
const AsyncSelector: FC<SelectorProperties> = (
    { url, placeholder, callback }: SelectorProperties
) => {

    // internal state depends on loaded options from fetch
    const [options, setOptions] = useState<string[]>([]);

    // fetch list of options on mount, track current flag
    // to prevent race conditions if component re-renders
    // and the hook is run again before previous fetch returns
    useEffect(() => {
        let isCurrentRequest = true;

        const fetchData = () => {
            return axios.get(url, getJSONHeader());
        }
    
        const updateOptions = () => {
            fetchData().then((response: any) => {
                if (isCurrentRequest)
                    setOptions(response.data);
            }).catch(e => {
                console.log(e);
            });
        }

        updateOptions();                       
        return () => {isCurrentRequest = false};
    }, [url]);

    return(
        <Select 
            className=" ml-4 mr-4" 
            placeholder={placeholder} 
            onChange={(event) => callback(event.target.value)}
        >
            {options.map((option) => 
                <MenuItem value={option} key={option}>{option}</MenuItem>)}
        </Select>
    );
};

export default AsyncSelector;