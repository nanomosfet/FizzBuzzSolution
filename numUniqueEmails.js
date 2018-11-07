/**
 * @param {string[]} emails
 * @return {number}
 */

var numUniqueEmails = function(emails) {
    const set = new Set()
    const res = []
    let local, domain, uniqueEmail,tmp
    for (let email of emails) {
        local = email.split('@')[0]
        domain = email.split('@')[1]
        
        local = local.replace(/\.+/g, '')
        local = local.split('+')[0]
        uniqueEmail = `${local}@${domain}`
        if (!set.has(uniqueEmail)) {
            set.add(uniqueEmail)
            res.push(uniqueEmail)
        }        
    }
    return set.size
};