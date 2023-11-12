"use client";
import axios from "axios";
import React, { FC, useState, useEffect } from "react";
import { MenuItem, Select } from "@mui/material";
import { getJSONHeader } from "@/app/utils/cookies";

interface SelectorProperties {
    url: string, 
    placeholder: string,
    onChange: (arg: any) => void
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
const AsyncSelector: FC<SelectorProperties> = ({ url, placeholder, onChange }: SelectorProperties) => {

    const [options, setOptions] = useState<string[]>([]);

    // call hook only once on load to grab formats
    useEffect(() => {
        const fetchData = () => {
            return axios.get(url, getJSONHeader());
        }
    
        const onUpdateOptions = () => {
            fetchData().then((response: any) => {
                if (isCurrentRequest)
                    setOptions(response.data);
            }).catch(e => {
                console.log(e);
            });
        }

        let isCurrentRequest = true;             // set current flag when component mounts and hook is run
        onUpdateOptions();                       // perform an async data fetch
        return () => {isCurrentRequest = false}; // reset on unmount to prevent race conditions if the component re-mounts before the data fetch completes.
    }, []);

    return(
        <Select 
            className=" ml-4 mr-4" 
            placeholder={placeholder} 
            onChange={(event) => onChange(event.target.value)}
        >
        {options.map((option) => <MenuItem value={option} key={option}>{option}</MenuItem>)}
        </Select>
    );
};

export default AsyncSelector;